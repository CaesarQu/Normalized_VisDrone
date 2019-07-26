#Written by Jon Patman
#Edited by Jeromy Yu
import os
import sys
import cv2
import numpy as np
import tensorflow as tf
import time
import threading


sys.path.append('lib/api')
sys.path.append('lib/api/slim')


from object_detection.utils import  label_map_util
from object_detection.utils import visualization_utils as vis_util

#device_id = sys.argv[1] 
image_name = sys.argv[1]
#output_dir = 'output' # sys.argv[2]
#image_names = os.listdir(image_dir)

HAR_CASCADE_PATH = 'lib/cascade/haarcascade_frontalface_alt2.xml'
PROFILE_CASCADE_PATH = 'lib/cascade/lbpcascade_profileface.xml'

########## API Initialization #############
OBJ_NAME = 'person'
#PATH_TO_TEST_IMAGES_DIR = image_dir
#MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
PATH_TO_CKPT = 'lib/model'+ '/frozen_inference_graph.pb'
PATH_TO_LABELS =  'lib/api/object_detection/data/mscoco_label_map.pbtxt' #os.path.join('object_detection/data','mscoco_label_map.pbtxt')
NUM_CLASSES = 90

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes = NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

class myThread(threading.Thread):
	def __init__(self, threadID, name, imgName):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name

	def detect_face(self,img,cascPath):
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		face_cascade = cv2.CascadeClassifier(cascPath)
		faces = face_cascade.detectMultiScale(
		gray,
		scaleFactor=1.05,
		minNeighbors=5,
		minSize=(5, 5),
		flags = cv2.CASCADE_SCALE_IMAGE
		)
		gray = None
		if(len(faces)==0):
			return None
		(x,y,w,h) = faces[0]
		faces = None
		face_cascade = None
		return (x,y,w,h)
   
	def run(self):
		start_time = time.time()

	############################################


		############## Load model into Tensorflow ###########################        
		detection_graph = tf.Graph()
		with detection_graph.as_default():
			od_graph_def = tf.GraphDef()
			with tf.gfile.GFile(PATH_TO_CKPT,'rb') as fid:
				serialized_graph = fid.read()
				od_graph_def.ParseFromString(serialized_graph)
				tf.import_graph_def(od_graph_def,name='')
		############## Load model into Tensorflow ###########################    



		############### Model Execution / Object Detection ###################

		with detection_graph.as_default():
			with tf.Session(graph=detection_graph) as sess:
				image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
				detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
				detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
				detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
				num_detections = detection_graph.get_tensor_by_name('num_detections:0')
				
				end_time = time.time()
				loading_time = round((end_time-start_time),4)
				start_time_total = time.time()
				
		############################# Step 1 - Preprocessing ###################
				start_time =  time.time()
				raw_image = cv2.imread(image_name)
				input_image = cv2.imread(image_name)
				 
				#Noise reduction using gaussian filtering
				image = cv2.GaussianBlur(raw_image,(5,5),0)
				
				# Histogram equalization
				img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
			
				# equalize the histogram of the Y channel
				img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
			
				# convert the YUV image back to RGB format
				image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

				end_time = time.time()
				step_1_time =round((end_time-start_time),4)
				#output_dir = img_name
				# if not os.path.exists('output/'+device_id):
				#     os.makedirs('output/'+device_id)
				# else:
				#     os.unlink('output/'+device_id)
					
				# if not os.path.exists('output/'+device_id+'/'+output_dir):
				#     os.makedirs('output/'+device_id+'/'+output_dir)
				# else:
				#     for file in os.listdir('output/'+device_id+'/'+output_dir):
				#         os.unlink('output/'+device_id+'/'+output_dir+'/'+file) 
				#cv2.imwrite('output/'+ img_name +'_processed.png',image)
		########################### End of step 1 ##############
			
		############################# Step 2 - Person Detection ###################
				start_time = time.time()
				image_np_expanded = np.expand_dims(image, axis=0)
				# Actual detection.
				(boxes, scores, classes, num) = sess.run(
				  [detection_boxes, detection_scores, detection_classes, num_detections],
				  feed_dict={image_tensor: image_np_expanded})
				
				# vis_util.visualize_boxes_and_labels_on_image_array(
				#   raw_image,
				#   np.squeeze(boxes),
				#   np.squeeze(classes).astype(np.int32),
				#   np.squeeze(scores),
				#   category_index,
				#   use_normalized_coordinates=True,
				#   line_thickness=8)
				im_width = raw_image.shape[0]
				im_height = raw_image.shape[1]
				class_count = {}
					
				#cv2.imwrite('output/'+ img_name +'_object_detection.png',raw_image)
				
				end_time = time.time()
				step_2_time = round((end_time-start_time),4)

		########################## End Step 2 - Person Detection ################### 

		# ############################ Step 3 - Face Detection ###################      
				start_time = time.time()
				num_of_face_detection = 0
				num_of_person_detected = 0
				face_list = []
				for index,value in enumerate(classes[0]):
					if(scores[0][index]>.5):
						class_name = category_index.get(value)['name']
						
					  #  if class_name != OBJ_NAME:
					  #      continue
						if class_name not in class_count:
							class_count[class_name] = 1
						else:
							class_count[class_name]+=1
						
						ymin = int(boxes[0,index,0]*im_width)
						xmin = int(boxes[0,index,1]*im_height)
						ymax = int(boxes[0,index,2]*im_width)
						xmax = int(boxes[0,index,3]*im_height)
						cropped_object = tf.image.crop_to_bounding_box(image,ymin,xmin,ymax-ymin,xmax-xmin).eval()
						num_of_person_detected += 1
						
						#cv2.imwrite('output/'+ img_name +'_'+class_name+'_'+str(class_count[class_name])+'.png', cropped_object)
		 
						box = self.detect_face(cropped_object,HAR_CASCADE_PATH)
						face_list.append(box)

				end_time = time.time()
				step_3_time = round((end_time-start_time),4)
				#cv2.imwrite('output/'+ img_name +'_4_final_output.jpg', input_image)
		################################## End of step 3 ############################################

		################################## Step 4 - Face Database Storage ############################
				start_time = time.time()
				for idx,box in enumerate(face_list):
					if box is not None:
						[x,y,w,h] = box
						#cropped_image_name = 'class_name'+'_'+str(class_count[class_name])+ '_face.png'
						num_of_face_detection+=1
						cv2.rectangle(input_image, (xmin+x, ymin+y), (xmin+x+w, ymin+y+h), (0, 255, 0), 2)
						cv2.putText(input_image, str(idx), (xmin+x, ymin+y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

				cv2.imwrite('output/imgWithFaces.png', input_image)
				end_time = time.time()
				step_4_time = round((end_time-start_time),4)

				#img_size = str(round(os.path.getsize(image_dir+"/"+device_id+'/'+image_name)/1024,2))+ " KB"
				img_height,img_width = raw_image.shape[:2]
				img_dim = str(img_width)+" * "+str(img_height)
				end_time_total = time.time()
				total_time = round((end_time_total-start_time_total),4)            
				statusRow = image_name+","+str(img_width)+","+str(img_height)+","+str(loading_time)+","+str(step_1_time)+","+str(step_2_time)+","+str(step_3_time)+"," +str(step_4_time) +","+ str(total_time)+","+str(num_of_person_detected)+","+str(num_of_face_detection)
				
				if self.name == "Thread-1":
					print(statusRow)  
	
# Create new threads
thread1 = myThread(1, "Thread-1", image_name)
#thread2 = myThread(2, "Thread-2", image_name)

# Start new Threads
thread1.start()
#thread2.start()
