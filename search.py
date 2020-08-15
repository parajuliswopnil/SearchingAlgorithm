import math


# linear search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i

    return -1

# binary search
def binarySearch(data, target):
    start = 0
    end = len(data)
    loopLength = len(data)
    for i in range(0, loopLength):
        mid_index = int(math.floor((start + end) / 2))
        mid_element = data[mid_index]
       # print('The mid index is:' + str(mid_index))

        if mid_element < target:
            start = mid_index

        elif mid_element > target:
            end = mid_index

        else:
            print('The element is ' + str(mid_element), 'present in the index ' + str(mid_index), 'of the array.')
            return mid_index
            break
