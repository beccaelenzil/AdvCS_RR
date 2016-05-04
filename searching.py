# Number of Operations
# --------------------
# Best Case: n
# Worst Case: n
# Average Case: n

def sequentialSearch(aList, value):
    return True if sum([1 if value == aList[x] else 0 for x in range(len(aList))]) != 0 else False

# Number of Operations
# --------------------
# Best Case: 1
# Worst Case: log(n)
# Average Case: log(n)
# Big-O of Binary Search
# O(log(n))
def binarySearch(aList, value):
    if len(aList) == 1:
        return True if value == aList[0] else False
    elif aList[len(aList)//2] == value:
        return True
    elif aList[len(aList)//2] < value:
        return binarySearch(aList[len(aList)//2:],value)
    elif aList[len(aList)//2] > value:
        return binarySearch(aList[:len(aList)//2],value)


print binarySearch(range(100),108)
