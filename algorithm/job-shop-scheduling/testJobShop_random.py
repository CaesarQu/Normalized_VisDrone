# Algorithm from Google OR
# Code Edited by Jeromy Yu and Chengyi Qu
from __future__ import print_function

import collections
import os
import sys
import random

# Import Python wrapper for or-tools CP-SAT solver.
from ortools.sat.python import cp_model
DataPath = os.path.expanduser("~/processing_data/dense")
DataPath1 = os.path.expanduser("~/processing_data/sparse/xoxlarge")

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

    random_1 = []
    random_2 = []
    random_3 = []
    random_4 = []
    random_5 = []
    random_6 = []
    random_7 = []
    random_8 = []
    random_9 = []
    random_10 = []
    random_11 = []
    random_12 = []
    random_13 = []
    random_14 = []
    random_15 = []
    random_16 = []
    random_17 = []
    random_18 = []
    random_19 = []
    random_20 = []

    time = 0.0

    for x in range(100):
        num = random.choice([0, 1])
        num2 = random.choice([0, 2])
        num3 = random.choice([0, 3])
        num4 = random.choice([0, 4])
        num5 = random.choice([0, 5])
        num6 = random.choice([0, 6])
        num7 = random.choice([0, 7])
        num8 = random.choice([0, 8])
        num9 = random.choice([0, 9])
        num10 = random.choice([0, 10])
        num11 = random.choice([0, 11])
        num12 = random.choice([0, 12])
        num13 = random.choice([0, 13])
        num14 = random.choice([0, 14])
        num15 = random.choice([0, 15])
        num16 = random.choice([0, 16])
        num17 = random.choice([0, 17])
        num18 = random.choice([0, 18])
        num19 = random.choice([0, 19])
        num20 = random.choice([0, 20])
        random_1.append(num)
        random_2.append(num2)
        random_3.append(num3)
        random_4.append(num4)
        random_5.append(num5)
        random_6.append(num6)
        random_7.append(num7)
        random_8.append(num8)
        random_9.append(num9)
        random_10.append(num10)
        random_11.append(num11)
        random_12.append(num12)
        random_13.append(num13)
        random_14.append(num14)
        random_15.append(num15)
        random_16.append(num16)
        random_17.append(num17)
        random_18.append(num18)
        random_19.append(num19)
        random_20.append(num20)

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
    for i in range(len(random_1)):
        pt1 = int((float(dense_xl1[index][func]) * 10))
        pt2 = int((float(dense_xl2[index][func]) * 10))
        pt3 = int((float(dense_xl3[index][func]) * 10))
        pt4 = int((float(dense_xl4[index][func]) * 10))
        pt5 = int((float(dense_xl5[index][func]) * 10))
        pt6 = int(round(float(dense_xl6[index][func]) * 1))
        pt7 = int(round(float(dense_xl7[index][func]) * 1))
        pt8 = int(round(float(dense_xl8[index][func]) * 1))
        pt9 = int(round(float(dense_xl9[index][func]) * 1))
        pt10 = int(round(float(dense_xl10[index][func]) * 1))
        pt11 = int(round(float(sparse_xl1[index][func]) * 1))
        pt12 = int(round(float(sparse_xl2[index][func]) * 1))
        pt13 = int(round(float(sparse_xl3[index][func]) * 1))
        pt14 = int(round(float(sparse_xl4[index][func]) * 1))
        pt15 = int(round(float(sparse_xl5[index][func]) * 1))
        pt16 = int(float(sparse_xl6[index][func]) * 1)
        pt17 = int(float(sparse_xl7[index][func]) * 1)
        pt18 = int(float(sparse_xl8[index][func]) * 1)
        pt19 = int(float(sparse_xl9[index][func]) * 1)
        pt20 = int(float(sparse_xl10[index][func]) * 1)
        
        if (func == 5):
            if (random_1[i] != 0):
                pt1 = pt1 * 20
            if (random_2[i] != 0):
                pt2 = pt2 * 20
            if (random_3[i] != 0):
                pt3 = pt3 * 20
            if (random_4[i] != 0):
                pt4 = pt4 * 20
            if (random_5[i] != 0):
                pt5 = pt5 * 20
            if (random_6[i] != 0):
                pt6 = pt6 * 20
            if (random_7[i] != 0):
                pt7 = pt7 * 20
            if (random_8[i] != 0):
                pt8 = pt8 * 20
            if (random_9[i] != 0):
                pt9 = pt9 * 20
            if (random_10[i] != 0):
                pt10 = pt10 * 20
            if (random_11[i] != 0):
                pt11 = pt11 * 20
            if (random_12[i] != 0):
                pt12 = pt12 * 20
            if (random_13[i] != 0):
                pt13 = pt13 * 20
            if (random_14[i] != 0):
                pt14 = pt14 * 20
            if (random_15[i] != 0):
                pt15 = pt15 * 20
            if (random_16[i] != 0):
                pt16 = pt16 * 20
            if (random_17[i] != 0):
                pt17 = pt17 * 20
            if (random_18[i] != 0):
                pt18 = pt18 * 20
            if (random_19[i] != 0):
                pt19 = pt19 * 20
            if (random_20[i] != 0):
                pt20 = pt20 * 20
        
        time = time + 0.2125 + pt1 + pt2 + pt3 + pt4 + pt5 + pt6 + pt7 + pt8 + pt9 + pt10 + pt11 + pt12 + pt13 + pt14 + pt15 + pt16 + pt17 + pt18 + pt19 + pt20
        jobs_data1.append((random_1[i], pt1))
        jobs_data2.append((random_2[i], pt2))
        jobs_data3.append((random_3[i], pt3))
        jobs_data4.append((random_4[i], pt4))
        jobs_data5.append((random_5[i], pt5))
        jobs_data6.append((random_6[i], pt6))
        jobs_data7.append((random_7[i], pt7))
        jobs_data8.append((random_8[i], pt8))
        jobs_data9.append((random_9[i], pt9))
        jobs_data10.append((random_10[i], pt10))
        jobs_data11.append((random_11[i], pt11))
        jobs_data12.append((random_12[i], pt12))
        jobs_data13.append((random_13[i], pt13))
        jobs_data14.append((random_14[i], pt14))
        jobs_data15.append((random_15[i], pt15))
        jobs_data16.append((random_16[i], pt16))
        jobs_data17.append((random_17[i], pt17))
        jobs_data18.append((random_18[i], pt18))
        jobs_data19.append((random_19[i], pt19))
        jobs_data20.append((random_20[i], pt20))

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
