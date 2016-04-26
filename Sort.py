import matplotlib.pyplot as plt
import random
import math

def randList(end):
    return random.sample([x for x in range(end)], end)

def bubSort(array):
    n=0
    k = len(array) - 1
    flip = True
    while flip == True:
        flip = False
        for i in range(k):
            n+=1
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                flip = True
        if not flip:
            break
        k-=1
    return n

def selectSort(array):
    n = 0
    for i in range(len(array)):
        listv = array[i]
        for j in range(i+1,len(array)):
            n+=1
            if listv > array[j]:
                listv, array[j] = array[j], listv
        array[i] = listv
    return n

def insertionSort(array):
    for i in range(len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    print array

def shellSort(array, dif):
    subArray = [[array[dif*i+j] for i in range(int((len(array)-j-1)/dif)+1)] for j in range(dif)]
    for i in range(len(subArray)):
        insertionSort(subArray[i])
    array = [subArray[i%dif][int(i/dif)] for i in range(len(array))]
    print array
    if not dif == 1:
        shellSort(array,int(dif/2))

def quickSort(array, start, stop):
    if stop-start < 1:
        return array
    else:
        left = start
        right = stop
        pivot = array[start]
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
                print array
        quickSort(array,start,right)
        quickSort(array,left,stop)

quickSort(randList(20),0,19)



#num_iter = []
#for i in range(100):
#    n = selectSort(randList(100))
#    num_iter.append(n)
#ave_iter = sum(num_iter)/len(num_iter)
#print ave_iter