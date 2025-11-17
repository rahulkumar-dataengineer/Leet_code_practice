'''
same as Insertion sort but works with larger gaps and reducing them down to insertion sort
Take an element and place it in its correct position
swap left side
'''

from helper.sort import print_help
arr = [10, 12, 8, 7, 61, 78, 13, 87, 2, 0, 5]
length = len(arr)


gap = length // 2

while gap > 0:
    for right in range(gap, length):
        temp = arr[right]
        left = right
        while left >= gap and arr[left - gap] > temp:
            # print_help(arr, left, left-1, [""]*length)
            arr[left] = arr[left - gap]
            left -= gap
            # print_help(arr, left, left-1, [""]*length)
        arr[left] = temp
    gap //= 2

print(arr)
