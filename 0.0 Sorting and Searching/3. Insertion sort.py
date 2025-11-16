'''
Take an element and place it in its correct position
swap left side
'''

from helper.sort import print_help
arr = [10, 12, 8, 7, 61, 78, 13, 87, 2, 0, 5]
length = len(arr)



for index in range(length):
    index2 = index
    while index2 >= 1 and arr[index2] < arr[index2-1]:
        # print_help(arr, index2, index2-1, [""]*length)
        arr[index2], arr[index2 - 1] = arr[index2 - 1], arr[index2]
        index2-=1
        # print_help(arr, index2, index2-1, [""]*length)

print(arr)

