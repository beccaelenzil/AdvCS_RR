import random

cnt = 0
for i in range(1000000):
    a  = [random.randrange(6) for x in range(6)]
    b = [0 for x in range(6)]
    for j in a:
        b[j] += 1
    if (b[1] == 2 and b[2] == 2 and b[3] == 2) or (b[1] == 2 and b[2] == 2 and b[5] == 2) or (b[1] == 2 and b[5] == 2 and b[3] == 2) or (b[5] == 2 and b[2] == 2 and b[3] == 2):
        print a
        print i
        cnt += 1
print cnt