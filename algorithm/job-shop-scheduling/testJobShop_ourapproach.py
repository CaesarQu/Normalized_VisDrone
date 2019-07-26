#Algorithm From Google OR
#Edited by Jeromy Yu and Chengyi Qu
from __future__ import print_function

import collections
import os
import sys
import random

# Import Python wrapper for or-tools CP-SAT solver.
from ortools.sat.python import cp_model
DataPath = os.path.expanduser("~/processing_data/dense")
DataPath1 = os.path.expanduser("~/processing_data/sparse/xoxlarge")
network_condition = 10

def setup(DataPath,filename):
    filePath = os.path.join(DataPath,filename)
    with open (filePath,"r") as F:
        data = F.read()
    data = data.splitlines()
    for i in range(len(data)):
        data[i] = data[i].split(',')
    return data

def MinimalJobshopSat():
    """Minimal jobshop problem."""
    # Create the model.
    model = cp_model.CpModel()
    DataPath_dense_m = os.path.join(DataPath, "xomedium")
    DataPath_dense_l = os.path.join(DataPath, "xolarge")
    DataPath_dense_xl = os.path.join(DataPath,"xoxlarge")
    dense_l1 = setup(DataPath_dense_l, "013_01073_v_xolarge.csv")
    dense_l2 = setup(DataPath_dense_l, "072_04488_v_xolarge.csv")
    dense_l3 = setup(DataPath_dense_l, "072_06432_v_xolarge.csv")
    dense_l4 = setup(DataPath_dense_l, "013_01392_v_xolarge.csv")
    dense_l5 = setup(DataPath_dense_l, "361_02323_v_xolarge.csv")
    dense_l6 = setup(DataPath_dense_l, "143_02250_v_xolarge.csv")
    dense_l7 = setup(DataPath_dense_l, "013_00000_v_xolarge.csv")
    dense_l8 = setup(DataPath_dense_l, "150_02310_v_xolarge.csv")
    dense_l9 = setup(DataPath_dense_l, "363_00001_v_xolarge.csv")
    dense_l10 = setup(DataPath_dense_xl, "084_00000_v_xoxlarge.csv")
    dense_xl1 = setup(DataPath_dense_xl, "013_01073_v_xoxlarge.csv")
    dense_xl2 = setup(DataPath_dense_xl, "072_04488_v_xoxlarge.csv")
    dense_xl3 = setup(DataPath_dense_xl, "072_06432_v_xoxlarge.csv")
    dense_xl4 = setup(DataPath_dense_xl, "013_01392_v_xoxlarge.csv")
    dense_xl5 = setup(DataPath_dense_xl, "361_02323_v_xoxlarge.csv")
    dense_xl6 = setup(DataPath_dense_xl, "143_02250_v_xoxlarge.csv")
    dense_xl7 = setup(DataPath_dense_xl, "013_00000_v_xoxlarge.csv")
    dense_xl8 = setup(DataPath_dense_xl, "150_02310_v_xoxlarge.csv")
    dense_xl9 = setup(DataPath_dense_xl, "363_00001_v_xoxlarge.csv")
    dense_xl10 = setup(DataPath_dense_xl, "084_00000_v_xoxlarge.csv")
    sparse_xl1 = setup(DataPath1, "071_03240_v_xoxlarge.csv")
    sparse_xl2 = setup(DataPath1, "071_03240_v_xoxlarge.csv")
    sparse_xl3 = setup(DataPath1, "308_01380_v_xoxlarge.csv")
    sparse_xl4 = setup(DataPath1, "329_04715_v_xoxlarge.csv")
    sparse_xl5 = setup(DataPath1, "352_05980_v_xoxlarge.csv")
    sparse_xl6 = setup(DataPath1, "072_05448_v_xoxlarge.csv")
    sparse_xl7 = setup(DataPath1, "079_00480_v_xoxlarge.csv")
    sparse_xl8 = setup(DataPath1, "020_00406_v_xoxlarge.csv")
    sparse_xl9 = setup(DataPath1, "300_00000_v_xoxlarge.csv")
    sparse_xl10 = setup(DataPath1, "099_02109_v_xoxlarge.csv")
    dense_m1 = setup(DataPath_dense_m, "XOMedium_Test1Dense.csv")
    dense_m2 = setup(DataPath_dense_m, "XOMedium_Test2Dense.csv")
    dense_m3 = setup(DataPath_dense_m, "XOMedium_Test3Dense.csv")
    dense_m4 = setup(DataPath_dense_m, "XOMedium_Test4Dense.csv")
    dense_m5 = setup(DataPath_dense_m, "XOMedium_Test5Dense.csv")
    dense_m6 = setup(DataPath_dense_m, "XOMedium_Test6Dense.csv")
    dense_m7 = setup(DataPath_dense_m, "XOMedium_Test7Dense.csv")
    dense_m8 = setup(DataPath_dense_m, "XOMedium_Test8Dense.csv")
    dense_m9 = setup(DataPath_dense_m, "XOMedium_Test9Dense.csv")
    dense_m10 = setup(DataPath_dense_m, "XOMedium_Test10Dense.csv")

    jobs_data = []
    jobs_data1 = []
    jobs_data2 = []
    jobs_data3 = []
    jobs_data4 = []
    jobs_data5 = []
    jobs_data6 = []
    jobs_data7 = []
    jobs_data8 = []
    jobs_data9 = []
    jobs_data10 = []
    jobs_data11 = []
    jobs_data12 = []
    jobs_data13 = []
    jobs_data14 = []
    jobs_data15 = []
    jobs_data16 = []
    jobs_data17 = []
    jobs_data18 = []
    jobs_data19 = []
    jobs_data20 = []
    index = 1
    func = 4
    num = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    count14 = 0
    count15 = 0
    count16 = 0
    count17 = 0
    count18 = 0
    count19 = 0
    count20 = 0
    time = 0.0
    for i in range(100):
        times = 2
        pt1 = int((float(dense_xl1[index][func]) * times))
        pt2 = int((float(dense_xl2[index][func]) * times))
        pt3 = int((float(dense_xl3[index][func]) * times))
        pt4 = int((float(dense_xl4[index][func]) * times))
        pt5 = int((float(dense_xl5[index][func]) * times))
        pt6 = int((float(dense_xl6[index][func]) * times))
        pt7 = int((float(dense_xl7[index][func]) * times))
        pt8 = int((float(dense_xl8[index][func]) * times))
        pt9 = int((float(dense_xl9[index][func]) * times))
        pt10 = int((float(dense_xl10[index][func]) * times))
        pt11 = int((float(sparse_xl1[index][func]) * times))
        pt12 = int((float(sparse_xl2[index][func]) * times))
        pt13 = int((float(sparse_xl3[index][func]) * times))
        pt14 = int((float(sparse_xl4[index][func]) * times))
        pt15 = int((float(sparse_xl5[index][func]) * times))
        pt16 = int((float(sparse_xl6[index][func]) * times))
        pt17 = int((float(sparse_xl7[index][func]) * times))
        pt18 = int((float(sparse_xl8[index][func]) * times))
        pt19 = int((float(sparse_xl9[index][func]) * times))
        pt20 = int((float(sparse_xl10[index][func]) * times))

        obj1 = int(dense_xl1[index][9])
        obj2 = int(dense_xl2[index][9])
        obj3 = int(dense_xl3[index][9])
        obj4 = int(dense_xl4[index][9])
        obj5 = int(dense_xl5[index][9])
        obj6 = int(dense_xl6[index][9])
        obj7 = int(dense_xl7[index][9])
        obj8 = int(dense_xl8[index][9])
        obj9 = int(dense_xl9[index][9])
        obj10 = int(dense_xl10[index][9])
        obj11 = int(sparse_xl1[index][9])
        obj12 = int(sparse_xl2[index][9])
        obj13 = int(sparse_xl3[index][9])
        obj14 = int(sparse_xl4[index][9])
        obj15 = int(sparse_xl5[index][9])
        obj16 = int(sparse_xl6[index][9])
        obj17 = int(sparse_xl7[index][9])
        obj18 = int(sparse_xl8[index][9])
        obj19 = int(sparse_xl9[index][9])
        obj20 = int(sparse_xl10[index][9])

        if (func == 4):
            jobs_data1.append((1, pt1))
            jobs_data2.append((2, pt2))
            jobs_data3.append((3, pt3))
            jobs_data4.append((4, pt4))
            jobs_data5.append((5, pt5))
            jobs_data6.append((6, pt6))
            jobs_data7.append((7, pt7))
            jobs_data8.append((8, pt8))
            jobs_data9.append((9, pt9))
            jobs_data10.append((10, pt10))
            jobs_data11.append((11, pt11))
            jobs_data12.append((12, pt12))
            jobs_data13.append((13, pt13))
            jobs_data14.append((14, pt14))
            jobs_data15.append((15, pt15))
            jobs_data16.append((16, pt16))
            jobs_data17.append((17, pt17))
            jobs_data18.append((18, pt18))
            jobs_data19.append((19, pt19))
            jobs_data20.append((20, pt20))

        if (func == 5):
            if (((network_condition == 10) & (count1 <= 42)) | ((network_condition == 5) & (count1 <= 34)) | ((network_condition == 1) & (count1 <= 14))):
                jobs_data1.append((0, pt1))
                #print(count1)
                count1 = count1 + 1
            else:
                pt1 = pt1 * 20
                jobs_data1.append((1, pt1))
            if (((network_condition == 10) & (count2 <= 42)) | ((network_condition == 5) & (count2 <= 34)) | ((network_condition == 1) & (count2 <= 14))):
                jobs_data2.append((0, pt2))
                count2 = count2 + 1
            else:
                pt2 = pt2 * 20
                jobs_data2.append((2, pt2))
            if (((network_condition == 10) & (count3 <= 42)) | ((network_condition == 5) & (count3 <= 34)) | ((network_condition == 1) & (count3 <= 14))):
                jobs_data3.append((0, pt3))
                count3 = count3 + 1
            else:
                pt3 = pt3 * 20
                jobs_data3.append((3,pt3))
            if (((network_condition == 10) & (count4 <= 42)) | ((network_condition == 5) & (count4 <= 34)) | ((network_condition == 1) & (count4 <= 14))):
                jobs_data4.append((0, pt4))
                #count = count + 1
            else:
                pt4 = pt4 * 20
                jobs_data4.append((4, pt4))
            if (((network_condition == 10) & (count5 <= 42)) | ((network_condition == 5) & (count5 <= 34)) | ((network_condition == 1) & (count5 <= 14))):
                jobs_data5.append((0, pt5))
                #count = count + 1
            else:
                pt5 = pt5 * 20
                jobs_data5.append((5, pt5))
            if (((network_condition == 10) & (count6 <= 42)) | ((network_condition == 5) & (count6 <= 34)) | ((network_condition == 1) & (count6 <= 14))):
                jobs_data6.append((0, pt6))
                #count = count + 1
            else:
                pt6 = pt6 * 20
                jobs_data6.append((6, pt6))
            if (((network_condition == 10) & (count7 <= 42)) | ((network_condition == 5) & (count7 <= 34)) | ((network_condition == 1) & (count7 <= 14))):
                jobs_data7.append((0, pt7))
                #count = count + 1
            else:
                pt7 = pt7 * 20
                jobs_data7.append((7, pt7))
            if (((network_condition == 10) & (count8 <= 42)) | ((network_condition == 5) & (count8 <= 34)) | ((network_condition == 1) & (count8 <= 14))):
                jobs_data8.append((0, pt8))
                #count = count + 1
            else:
                pt8 = pt8 * 20
                jobs_data8.append((8, pt8))
            if (((network_condition == 10) & (count9 <= 42)) | ((network_condition == 5) & (count9 <= 34)) | ((network_condition == 1) & (count9 <= 14))):
                jobs_data9.append((0, pt9))
                #count = count + 1
            else:
                pt9 = pt9 * 20
                jobs_data9.append((9, pt9))
            if (((network_condition == 10) & (count10 <= 42)) | ((network_condition == 5) & (count10 <= 34)) | ((network_condition == 1) & (count10 <= 14))):
                jobs_data10.append((0, pt10))
                #count = count + 1
            else:
                pt10 = pt10 * 20
                jobs_data10.append((10, pt10))
            if (((network_condition == 10) & (count11 <= 42)) | ((network_condition == 5) & (count11 <= 34)) | ((network_condition == 1) & (count11 <= 14))):
                jobs_data11.append((0, pt11))
                #count = count + 1
            else:
                pt11 = pt11 * 20
                jobs_data11.append((11, pt11))
            if (((network_condition == 10) & (count12 <= 42)) | ((network_condition == 5) & (count12 <= 34)) | ((network_condition == 1) & (count12 <= 14))):
                jobs_data12.append((0, pt12))
                #count = count + 1
            else:
                pt12 = pt12 * 20
                jobs_data12.append((12, pt12))
            if (((network_condition == 10) & (count13 <= 42)) | ((network_condition == 5) & (count13 <= 34)) | ((network_condition == 1) & (count13 <= 14))):
                jobs_data13.append((0, pt13))
                #count = count + 1
            else:
                pt13 = pt13 * 20
                jobs_data13.append((13, pt13))
            if (((network_condition == 10) & (count14 <= 42)) | ((network_condition == 5) & (count14 <= 34)) | ((network_condition == 1) & (count14 <= 14))):
                jobs_data14.append((0, pt14))
                #count = count + 1
            else:
                pt14 = pt14 * 20
                jobs_data14.append((14, pt14))
            if (((network_condition == 10) & (count15 <= 42)) | ((network_condition == 5) & (count15 <= 34)) | ((network_condition == 1) & (count15 <= 14))):
                jobs_data15.append((0, pt15))
                #count = count + 1
            else:
                pt15 = pt15 * 20
                jobs_data15.append((15, pt15))
            if (((network_condition == 10) & (count16 <= 42)) | ((network_condition == 5) & (count16 <= 34)) | ((network_condition == 1) & (count16 <= 14))):
                jobs_data16.append((0, pt16))
                #count = count + 1
            else:
                pt16 = pt16 * 20
                jobs_data16.append((16, pt16))
            if (((network_condition == 10) & (count17 <= 42)) | ((network_condition == 5) & (count17 <= 34)) | ((network_condition == 1) & (count17 <= 14))):
                jobs_data17.append((0, pt17))
                #count = count + 1
            else:
                pt17 = pt17 * 20
                jobs_data17.append((17, pt17))
            if (((network_condition == 10) & (count18 <= 42)) | ((network_condition == 5) & (count18 <= 34)) | ((network_condition == 1) & (count18 <= 14))):
                jobs_data18.append((0, pt18))
                #count = count + 1
            else:
                pt18 = pt18 * 20
                jobs_data18.append((18, pt18))
            if (((network_condition == 10) & (count19 <= 42)) | ((network_condition == 5) & (count19 <= 34)) | ((network_condition == 1) & (count19 <= 14))):
                jobs_data19.append((0, pt19))
                #count = count + 1
            else:
                pt19 = pt19 * 20
                jobs_data19.append((19, pt19))
            if (((network_condition == 10) & (count20 <= 42)) | ((network_condition == 5) & (count20 <= 34)) | ((network_condition == 1) & (count20 <= 14))):
                jobs_data20.append((0, pt20))
                #count = count + 1
            else:
                pt20 = pt20 * 20
                jobs_data20.append((20, pt20))

        if (func == 6):
            if (obj1 > 1):
                jobs_data1.append((0, pt1))
            else:
                jobs_data1.append((1, pt1))
            if (obj2 > 1):
                jobs_data2.append((0, pt2))
            else:
                jobs_data2.append((2, pt2))
            if (obj3 > 1):
                jobs_data3.append((0, pt3))
            else:
                jobs_data3.append((3, pt3))
            if (obj4 > 1):
                jobs_data4.append((0, pt4))
            else:
                jobs_data4.append((4, pt4))
            if (obj5 > 1):
                jobs_data5.append((0, pt5))
            else:
                jobs_data5.append((5, pt5))
            if (obj6 > 1):
                jobs_data6.append((0, pt6))
            else:
                jobs_data6.append((6, pt6))
            if (obj7 > 1):
                jobs_data7.append((0, pt7))
            else:
                jobs_data7.append((7, pt7))
            if (obj8 > 1):
                jobs_data8.append((0, pt8))
            else:
                jobs_data8.append((8, pt8))
            if (obj9 > 1):
                jobs_data9.append((0, pt9))
            else:
                jobs_data9.append((9, pt9))
            if (obj10 > 1):
                jobs_data10.append((0, pt10))
            else:
                jobs_data10.append((10, pt10))
            if (obj11 > 1):
                jobs_data11.append((0, pt11))
            else:
                jobs_data11.append((11, pt11))
            if (obj12 > 1):
                jobs_data12.append((0, pt12))
            else:
                jobs_data12.append((12, pt12))
            if (obj13 > 1):
                jobs_data13.append((0, pt13))
            else:
                jobs_data13.append((13, pt13))
            if (obj14 > 1):
                jobs_data14.append((0, pt14))
            else:
                jobs_data14.append((14, pt14))
            if (obj15 > 1):
                jobs_data15.append((0, pt15))
            else:
                jobs_data15.append((15, pt15))
            if (obj16 > 1):
                jobs_data16.append((0, pt16))
            else:
                jobs_data16.append((16, pt16))
            if (obj17 > 1):
                jobs_data17.append((0, pt17))
            else:
                jobs_data17.append((17, pt17))
            if (obj18 > 1):
                jobs_data18.append((0, pt18))
            else:
                jobs_data18.append((18, pt18))
            if (obj19 > 1):
                jobs_data19.append((0, pt19))
            else:
                jobs_data19.append((19, pt19))
            if (obj20 > 1):
                jobs_data20.append((0, pt20))
            else:
                jobs_data20.append((20, pt20))

        # (func == 7) is ignored because time is close to zero

        time = time + 0.2125 + pt1 + pt2 + pt3 + pt4 + pt5 + pt6 + pt7 + pt8 + pt9 + pt10 + pt11 + pt12 + pt13 + pt14 + pt15 + pt16 + pt17 + pt18 + pt19 + pt20

        #index = index + 1
        func = func + 1
        num = num + 1
        if ((num % 4) == 0):
            index = index + 1
        if (func > 7):
            func = 4
    print(time)

    jobs_data.append(jobs_data1)
    jobs_data.append(jobs_data2)
    jobs_data.append(jobs_data3)
    jobs_data.append(jobs_data4)
    jobs_data.append(jobs_data5)
    jobs_data.append(jobs_data6)
    jobs_data.append(jobs_data7)
    jobs_data.append(jobs_data8)
    jobs_data.append(jobs_data9)
    jobs_data.append(jobs_data10)
    jobs_data.append(jobs_data11)
    jobs_data.append(jobs_data12)
    jobs_data.append(jobs_data13)
    jobs_data.append(jobs_data14)
    jobs_data.append(jobs_data15)
    jobs_data.append(jobs_data16)
    jobs_data.append(jobs_data17)
    jobs_data.append(jobs_data18)
    jobs_data.append(jobs_data19)
    jobs_data.append(jobs_data20)

    #jobs_data = [  # task = (machine_id, processing_time).
     #   [(2, 274), (0, 20804), (1, 12269), (2,1), (0,33697), (1,16713),(1,12163), (2,1),(2,273),(2,16522),(1,6051),(1,453),(0,387),(1,18064),(2,18283),(0,44),(2,294),(0,19072),(0,17825),(0,482)],  # Job0
      #  [(1,1215), (2,17418), (0,4), (0,2272), (2,1189), (0,18302), (2,5), (0,2155), (2,1171), (1,17736), (1,4), (1,2217), (1,1130), (2,16549), (2,4), (1,2112), (0,1472), (2,17499), (2,4), (1,2095)],  # Job1
       # [(0,685), (2,16216), (2,2923), (1,1043), (0,722), (0,18054), (2,3041), (1,1043), (2,540), (0,17569), (0,3323), (2,1), (1,577), (2,16596), (2,2865), (0,1166), (1,570), (1,16744), (0,3535), (1,1101)]  # Job2
    #]

    machines_count = 1 + max(task[0] for job in jobs_data for task in job)
    all_machines = range(machines_count)

    # Computes horizon dynamically as the sum of all durations.
    horizon = sum(task[1] for job in jobs_data for task in job)

    # Named tuple to store information about created variables.
    task_type = collections.namedtuple('task_type', 'start end interval')
    # Named tuple to manipulate solution information.
    assigned_task_type = collections.namedtuple('assigned_task_type',
                                                'start job index duration')

    # Creates job intervals and add to the corresponding machine lists.
    all_tasks = {}
    machine_to_intervals = collections.defaultdict(list)

    for job_id, job in enumerate(jobs_data):
        for task_id, task in enumerate(job):
            machine = task[0]
            duration = task[1]
            suffix = '_%i_%i' % (job_id, task_id)
            start_var = model.NewIntVar(0, horizon, 'start' + suffix)
            end_var = model.NewIntVar(0, horizon, 'end' + suffix)
            interval_var = model.NewIntervalVar(start_var, duration, end_var,
                                                'interval' + suffix)
            all_tasks[job_id, task_id] = task_type(
                start=start_var, end=end_var, interval=interval_var)
            machine_to_intervals[machine].append(interval_var)


    # Create and add disjunctive constraints.
    for machine in all_machines:
        model.AddNoOverlap(machine_to_intervals[machine])

    # Precedences inside a job.
    for job_id, job in enumerate(jobs_data):
        for task_id in range(len(job) - 1):
            model.Add(all_tasks[job_id, task_id +
                                1].start >= all_tasks[job_id, task_id].end)

    # Makespan objective.
    obj_var = model.NewIntVar(0, horizon, 'makespan')
    model.AddMaxEquality(obj_var, [
        all_tasks[job_id, len(job) - 1].end
        for job_id, job in enumerate(jobs_data)
    ])
    model.Minimize(obj_var)

    # Solve model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL:
        # Create one list of assigned tasks per machine.
        assigned_jobs = collections.defaultdict(list)
        for job_id, job in enumerate(jobs_data):
            for task_id, task in enumerate(job):
                machine = task[0]
                assigned_jobs[machine].append(
                    assigned_task_type(
                        start=solver.Value(all_tasks[job_id, task_id].start),
                        job=job_id,
                        index=task_id,
                        duration=task[1]))

        # Create per machine output lines.
        output = ''
        for machine in all_machines:
            # Sort by starting time.
            assigned_jobs[machine].sort()
            sol_line_tasks = 'Machine ' + str(machine) + ': '
            sol_line = '           '

            for assigned_task in assigned_jobs[machine]:
                name = 'job_%i_%i' % (assigned_task.job, assigned_task.index)
                # Add spaces to output to align columns.
                sol_line_tasks += '%-10s' % name

                start = assigned_task.start
                duration = assigned_task.duration
                sol_tmp = '[%i,%i]' % (start, start + duration)
                # Add spaces to output to align columns.
                sol_line += '%-10s' % sol_tmp

            sol_line += '\n'
            sol_line_tasks += '\n'
            output += sol_line_tasks
            output += sol_line

        # Finally print the solution found.
        print('Optimal Schedule Length: %i' % solver.ObjectiveValue())
        print(output)


MinimalJobshopSat()
