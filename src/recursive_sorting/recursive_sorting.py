import math


# TO-DO: complete the helpe function below to merge 2 sorted arrays

# create an empty array
# use a while loop to check when the two length(left, right) is not zero
# check if the first element in the left array is less or equal to the first element on the right array.
# if it is, remove it from the left array and add it to the new array we created
# if not, do it for the right array
# add the last values and return the new array
# ps. u can use the *args operator in python

def merge(arrA, arrB):
    sorted_array = []
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # TO-DO

    while len(arrA) and len(arrB) != 0:
        if arrA[0] <= arrB[0]:
            sorted_array.append(arrA.pop(0))
        else:
           sorted_array.append(arrB.pop(0))

    return [*sorted_array, *arrA, *arrB]


# TO-DO: implement the Merge Sort function below USING RECURSION

# add a base case that checks if the length of the array is less than 2, because if it is, it means the array is already sorted
# if its not, find the middle of the array
# from the middle, get all from 0 to the middle for left
# repeat same for right
# make a recursive call to merge

def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr

    arr_middle = math.ceil(len(arr) / 2)

    arr_start = arr[0:arr_middle]
    arr_end = arr[arr_middle:]

    start = merge_sort(arr_start)
    end = merge_sort(arr_end)

    return merge(start, end)


print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
