'''
Get min from entire array -> swap with index

O(N^2)
'''
from helper.sort import print_help
arr = [10, 12, 8, 7, 61, 78, 13, 87, 2, 0, 5]
length = len(arr)


for index in range(length):
    minimum = index
    for index2 in range(index+1, length):
        if arr[index2] < arr[minimum]:
            minimum = index2
    # print_help(arr, index, minimum, [""]*length)
    arr[index], arr[minimum] = arr[minimum], arr[index]
    # print_help(arr, index, minimum, [""]*length)

# print(arr)