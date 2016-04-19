
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

bubSort([1,2,6,3,4,5])