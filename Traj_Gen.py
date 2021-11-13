import numpy as np
import math

# Traj 1
x1 = []
x1 = np.arange(333.5, 270, -5).tolist()
x1_len = len(x1)
y1 = np.zeros(x1_len)
y1 = y1.tolist()
traj1 = [x1, y1]

# Traj 2
y2 = np.arange(0, 50, 5).tolist()
x2 = []
for i in y2:
    x2_temp = 15 * math.sin(5 * i)
    x2_temp = x2_temp + 270
    x2.append(x2_temp)
traj2 = [x2, y2]

#Traj 3
y3 = np.arange(50, 150, 5).tolist()
x2_len = len(x2)
y3_len = len(y3)
x3 = x2[x2_len - 1]
x3_temp = np.ones(y3_len)
x3_temp = x3_temp.tolist()
x3 = [i * x2[x2_len-1] for i in x3_temp]
traj3 = [x3, y3]

#Traj 4
y4 = np.arange(150, 200, 5).tolist()
x3_len = len(x3)
x4 = []
for i in y2:
    x4_temp = -15 * math.sin(5 * i)
    x4_temp = x4_temp + x3[x3_len-1]
    x4.append(x4_temp)
traj4 = [x4, y4]

#Traj 5
x4_len = len(x4)
x5 = np.arange(x4[x4_len -1], 333.5, 5).tolist()
x5_len = len(x5)
y4_len = len(y4)
y5_temp = np.ones(x5_len).tolist()
y5 = [i * y4[y4_len-1] for i in y5_temp]
traj5 = [x5, y5]

# Combine Traj
traj_x = traj1[0] + traj2[0] + traj3[0] + traj4[0] + traj5[0]
traj_y = traj1[1] + traj2[1] + traj3[1] + traj4[1] + traj5[1]
traj = [traj_x, traj_y]