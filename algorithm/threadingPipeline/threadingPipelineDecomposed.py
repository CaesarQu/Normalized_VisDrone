#written by Jon Patman
#edited by Jeromy Yu
import os
import sys
import cv2
import numpy as np
import tensorflow as tf
import time
import threading
import requests
import random
import json

sys.path.append('lib/api')
sys.path.append('lib/api/slim')

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from flask import Flask, request, url_for, send_file, Response, jsonify
from flask_restful import Resource, Api
from collections import OrderedDict

# device_id = sys.argv[1]
#image_name = sys.argv[1]
# output_dir = 'output' # sys.argv[2]
# image_names = os.listdir(image_dir)

HAR_CASCADE_PATH = 'lib/cascade/haarcascade_frontalface_alt2.xml'
PROFILE_CASCADE_PATH = 'lib/cascade/lbpcascade_profileface.xml'

########## API Initialization #############
OBJ_NAME = 'person'
# PATH_TO_TEST_IMAGES_DIR = image_dir
# MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
PATH_TO_CKPT = 'lib/model' + '/frozen_inference_graph.pb'
PATH_TO_LABELS = 'lib/api/object_detection/data/mscoco_label_map.pbtxt'  # os.path.join('object_detection/data','mscoco_label_map.pbtxt')
NUM_CLASSES = 90

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)

app = Flask(__name__)


class myThread(threading.Thread):
    def __init__(self, threadID, name, imgName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name


def detect_face(img, cascPath):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cascPath)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    gray = None
    if (len(faces) == 0):
        return None
    (x, y, w, h) = faces[0]
    faces = None
    face_cascade = None
    return (x, y, w, h)

@app.route("/test",methods=["POST"])
def test():
    return request.json

@app.route("/Preprocessing",methods=["POST"])
def Preprocessing():
    start_time_total = time.time()
    start_time = time.time()
    file = request.json
    image_name = file["image_name"]
    # return image_name
    raw_image = cv2.imread(image_name)
    input_image = cv2.imread(image_name)

    # Noise reduction using gaussian filtering
    image = cv2.GaussianBlur(raw_image, (5, 5), 0)

    # Histogram equalization
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    # equalize the histogram of the Y channel
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

    # convert the YUV image back to RGB format
    image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    end_time = time.time()
    step_1_time = round((end_time - start_time), 4)
    # return Response(status=200)
    dict1 = {
        "start_time_total": start_time_total,
        "step_1_time": step_1_time,
        "image_name": image_name
    }
    cv2.imwrite("image.jpg",image)
    cv2.imwrite("raw_image.jpg",raw_image)
    cv2.imwrite("input_image.jpg",input_image)
    return dict1
    #return image, raw_image, input_image, start_time_total, step_1_time, image_name

@app.route("/PersonDetection",methods=["POST"])
def PersonDetection():
    start_time = time.time()
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            end_time = time.time()
            loading_time = round((end_time - start_time), 4)
    start_time = time.time()
    files = request.json
    image = files["image"]
    raw_image = files["raw_image"]
    image = cv2.imread(image)
    raw_image = cv2.imread(raw_image)
    # image, raw_image = request.json
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

    # cv2.imwrite('output/'+ img_name +'_object_detection.png',raw_image)

    end_time = time.time()
    step_2_time = round((end_time - start_time), 4)
    np.savetxt('boxes.txt', boxes[0], delimiter=', ')
    np.savetxt('scores.txt', scores, delimiter=', ')
    np.savetxt('classes.txt', classes, delimiter=', ')
    np.savetxt('num.txt', num, delimiter=', ')
    dict2 = {
        "im_width": im_width,
        "im_height": im_height,
        "class_count": class_count,
        "step_2_time": step_2_time,
        "loading_time": loading_time
    }
    return dict2
    # return boxes, scores, classes, num, im_width, im_height, class_count, step_2_time, loading_time


@app.route("/FaceDetection",methods=["POST"])
def FaceDetection():
    # image, boxes, scores, classes, num, im_width, im_height, class_count = request.json
    start_time = time.time()
    files = request.json
    image = files['image']
    boxes = files['boxes']
    scores = files['scores']
    classes = files['classes']
    num = files['num']
    dict2 = files['dict2']
    image = cv2.imread(image)
    boxes = np.loadtxt(boxes, delimiter=', ')
    scores = np.loadtxt(scores, delimiter=', ')
    classes = np.loadtxt(classes, delimiter=', ')
    num = np.loadtxt(num, delimiter=', ')
    with open(dict2, "r") as F:
        dict2 = F.read()
    dict2 = json.loads(dict2)
    #return dict2
    im_width = dict2['im_width']
    im_height = dict2['im_height']
    class_count = dict2['class_count']
    num_of_face_detection = 0
    num_of_person_detected = 0
    face_list = []
    for index, value in enumerate(classes):
        if (scores[index] > .5):
            class_name = category_index.get(value)['name']

            #  if class_name != OBJ_NAME:
            #      continue
            if class_name not in class_count:
                class_count[class_name] = 1
            else:
                class_count[class_name] += 1

            ymin = int(boxes[index, 0] * im_width)
            xmin = int(boxes[index, 1] * im_height)
            ymax = int(boxes[index, 2] * im_width)
            xmax = int(boxes[index, 3] * im_height)
            cropped_object = tf.image.crop_to_bounding_box(image, ymin, xmin, ymax - ymin,
                                                           xmax - xmin)  # .eval()
            num_of_person_detected += 1

            # cv2.imwrite('output/'+ img_name +'_'+class_name+'_'+str(class_count[class_name])+'.png', cropped_object)

            box = detect_face(image, HAR_CASCADE_PATH)
            face_list.append(box)
    end_time = time.time()
    step_3_time = round((end_time - start_time), 4)
    # print (face_list)
    with open('face_list.txt', 'w') as F0:
        for item in face_list:
            item = str(item)
            F0.write("%s\n" % item)
    dict3 = {
        #"face_list": face_list,
        "num_of_face_detection": num_of_face_detection,
        "num_of_person_detected": num_of_person_detected,
        "xmin": xmin,
        "xmax": xmax,
        "ymin": ymin,
        "ymax": ymax,
        "step_3_time": step_3_time
    }
    #return "good"
    return dict3
    #return face_list, num_of_face_detection, num_of_person_detected, xmin, xmax, ymin, ymax, step_3_time


@app.route("/DataBaseStorage",methods=["POST"])
def DataBaseStorage():
    #loading_time, image_name, step_1_time, step_2_time, step_3_time, start_time_total, input_image, raw_image, face_list, num_of_face_detection, num_of_person_detected, xmin, xmax, ymin, ymax = request.json
    start_time = time.time()
    files = request.json
    input_image = files['input_image']
    raw_image = files['raw_image']
    dict1 = files['dict1']
    dict2 = files['dict2']
    dict3 = files['dict3']
    input_image = cv2.imread(input_image)
    raw_image = cv2.imread(raw_image)
    with open(dict1, "r") as F1:
        dict1 = F1.read()
    with open(dict2, "r") as F2:
        dict2 = F2.read()
    with open(dict3, "r") as F3:
        dict3 = F3.read()
    dict1 = json.loads(dict1)
    dict2 = json.loads(dict2)
    dict3 = json.loads(dict3)
    start_time_total = dict1['start_time_total']
    step_1_time = dict1['step_1_time']
    image_name = dict1['image_name']
    step_2_time = dict2['step_2_time']
    loading_time = dict2['loading_time']
    with open('face_list.txt', 'r') as F4:
        face_list = F4.read()
    face_list = face_list.splitlines()
    # print(face_list)
    # return "good"
    # face_list = dict3['face_list']
    num_of_face_detection = dict3['num_of_face_detection']
    num_of_person_detected = dict3['num_of_person_detected']
    xmin = dict3['xmin']
    xmax = dict3['xmax']
    ymin = dict3['ymin']
    ymax = dict3['ymax']
    step_3_time = dict3['step_3_time']
    for idx, box in enumerate(face_list):
        if box is not None:
            # [x, y, w, h] = box
            # cropped_image_name = 'class_name'+'_'+str(class_count[class_name])+ '_face.png'
            num_of_face_detection += 1
            # cv2.rectangle(input_image, (xmin + x, ymin + y), (xmin + x + w, ymin + y + h), (0, 255, 0), 2)
            # cv2.putText(input_image, str(idx), (xmin + x, ymin + y), cv2.FONT_HERSHEY_PLAIN, 1.5,
              #          (0, 255, 0), 2)

    cv2.imwrite('output/imgWithFaces.png', input_image)
    end_time = time.time()
    step_4_time = round((end_time - start_time), 4)

    # img_size = str(round(os.path.getsize(image_dir+"/"+device_id+'/'+image_name)/1024,2))+ " KB"
    img_height, img_width = raw_image.shape[:2]
    img_dim = str(img_width) + " * " + str(img_height)
    end_time_total = time.time()
    # total_time = round((end_time_total - start_time_total), 4)
    total_time = round(step_1_time + step_2_time + step_3_time + step_4_time, 4)
    statusRow = image_name + "," + str(img_width) + "," + str(img_height) + "," + str(
        loading_time) + "," + str(step_1_time) + "," + str(step_2_time) + "," + str(
        step_3_time) + "," + str(step_4_time) + "," + str(total_time) + "," + str(
        num_of_person_detected) + "," + str(num_of_face_detection)

    return statusRow

#thread1 = myThread(1, "Thread-1", image_name)
# thread2 = myThread(2, "Thread-2", image_name)

# Start new Threads
#thread1.start()
# thread2.start()
