'''
Opposite to selection sort
pushes the largest element to last by adjacent swapping
inner loop runs length-index-1

O(N^2) - Worst and average
O(N) - best case
'''
from helper.sort import print_help
arr = [10, 12, 8, 7, 61, 78, 13, 87, 2, 0, 5]
length = len(arr)



for index in range(length):
    print(index)
    for index2 in range(length-index-1):
        swapped = False
        if arr[index2] > arr[index2 + 1]:
            # print_help(arr, index2, index2+1, [""]*length)
            arr[index2], arr[index2 + 1] = arr[index2 + 1], arr[index2]
            # print_help(arr, index2, index2+1, [""]*length)
            swapped = True
    if swapped == False:
        break

print(arr)

