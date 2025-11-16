'''
Pick a pivot element and place it in its correct place of the sorted array
- smaller on the left and larger on right
- left = low and right = high 
- compare left with pivot - stop where left>pivot
- opposite, stop where right<pivot
- swap left and right
- do this till left<=right
'''
from helper.sort import print_help
arr = [10, 12, 8, 7, 61, 78, 13, 87, 2, 0, 5]
length = len(arr)

def findPartition(arr, low, high):
    left = low
    right = high

    pivot = arr[left]
    

    while left < right:
        while arr[left] <= pivot and left < high:
            left+=1
        while arr[right] > pivot and right > low:
            right-=1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    
    return right


def quickSort(arr, low, high):
    if low >= high:
        return 
    
    if low < high:
        pivot = findPartition(arr, low, high)
        quickSort(arr,0, pivot-1)
        quickSort(arr,pivot+1, high)

    return arr


print(quickSort(arr, 0, length-1))
        
