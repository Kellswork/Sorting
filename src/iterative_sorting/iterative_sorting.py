# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # check the first item in the array
    # compare the first item in the array with the second item in the array
    # if the first item is bigger than the second item, replace the second item with the position of the second item

    # loop through n-1 elements

    # TO-DO: find next smallest element
    # (hint, can do in 3 loc)
    # TO-DO: swap

    new_arr = []
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
