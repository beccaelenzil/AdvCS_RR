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

def mergeSort(array):
    print "Splitting ",array
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k]=lefthalf[i]
                i=i+1
            else:
                array[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            array[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            array[k]=righthalf[j]
            j=j+1
            k=k+1
    print "Merging ",array

def mergeMyWay(array):
    array = [[array[x]] for x in range(len(array))]
    print array
    return mergeRecurse(array)[0]

def mergeRecurse(array):
    for i in range(len(array)//2):
        merge(array,i)
    print array
    if len(array) == 1:
        return array
    return mergeRecurse(array)

def merge(array, index):
    array[index] = [(array[index+1].pop(0) if len(array[index])==0 else array[index].pop(0))\
                        if len(array[index]) == 0 or len(array[index+1]) == 0 else\
                        (array[index].pop(0) if array[index][0] < array[index+1][0] else array[index+1].pop(0)) for i in range(len(array[index])+len(array[index+1]))]
    array.pop(index+1)
"""
array = randList(10)
print array
array = [[array[x]] for x in range(len(array))]
print array
mergeRecurse(array)
print array
"""
#myList = randList(10)
#myList = mergeMyWay(myList)
#print myList
y = [i for i in range(20,100,3)]
x = [i for i in range(len(y))]
plt.scatter(x,y)
plt.show()