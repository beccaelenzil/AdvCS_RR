import matplotlib.pyplot as plt


def bubSort(array):
    k = len(array) - 1
    flip = True
    while flip == True:
        flip = False
        for i in range(k):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                flip = True
        if not flip:
            break
    print array

def selectSort(array):
    for i in range(len(array)):
        listv = array[i]
        for j in range(i,len(array)):
            if listv > array[j]:
                listv, array[j] = array[j], listv
        array[i] = listv
    print array

y = [x for x in range(20,100,3)]
x = [x for x in range(len(y))]
plt.scatter(x,y)
plt.show()

selectSort([1,2,3,6,4,5])