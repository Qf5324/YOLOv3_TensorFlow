import random

ran = []
for i in range(1000):
    ran.append(random.randint(0, 7480))

with open('kitti_train.txt', 'w') as f:
    for i in range(7481):
        if i not in ran:
            if len(str(i)) == 1:
                j = '00000'+str(i)
            if len(str(i)) == 2:
                j = '0000' + str(i)
            if len(str(i)) == 3:
                j = '000'+str(i)
            if len(str(i)) == 4:
                j = '00'+str(i)
            f.write(j+'\n')

with open('kitti_val.txt', 'w') as f:
    for i in ran:
            if len(str(i)) == 1:
                j = '00000'+str(i)
            if len(str(i)) == 2:
                j = '0000' + str(i)
            if len(str(i)) == 3:
                j = '000'+str(i)
            if len(str(i)) == 4:
                j = '00'+str(i)
            f.write(j+'\n')