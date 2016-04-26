def badMin(array):
    """iterates and checks if every other entry in the list is less than the selected value i
    """
    for i in range(len(array)):
        min = array[i]
        if sum([0 if min <= array[j] else 1 for j in range(len(array))]) == 0:
            return min

def goodMin(array):
    """replaces stored value with the next value in the list if it is less than the stored value
    """
    min = array[0]
    for i in range(len(array)):
        if min > array[i]:
            min = array[i]
    return min

print goodMin([9,4,1,5,7])



