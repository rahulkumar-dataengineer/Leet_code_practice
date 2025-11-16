'''
Divide and merge
- split array into half till there is only 1 element
- merge 2 arrays(or indexes)
'''

from helper.sort import print_help
arr = [10, 12, 8, 7, 61, 78, 13, 87, 2, 0, 5]
length = len(arr)

def merge(arr, low, mid, high):
    result = []
    left, right = low, mid+1
    
    while left <= mid and right<=high:
        if arr[left] <= arr[right]:
            result.append(arr[left])
            left+=1
        else:
            result.append(arr[right])
            right+=1
    
    while left <= mid:
        result.append(arr[left])
        left+=1
    while right <= high:
        result.append(arr[right])
        right+=1
    arr[low:high+1] = result


def mergeSort(arr, low, high):
    if low >= high:
        return
    
    mid = (low + high) // 2
    
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)
    
    return arr

print(mergeSort(arr, 0, len(arr)-1))