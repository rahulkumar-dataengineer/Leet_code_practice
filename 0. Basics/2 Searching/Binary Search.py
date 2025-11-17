'''
when to apply

1. Space - Sorted or monotonic function/array or Bounded answer range
2. Problem can be expressed as a yes/no question
3. Ability to discard half the space each iteration
4. Searching for extremal (min/max) values or target - consider binary search over the answer space
'''

def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



def recursiveBinarySearch(arr, target, left, right):
    # base case
    if left > right:
        return -1
    
    mid = left + (right - left) // 2  

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursiveBinarySearch(arr, target, mid+1, right)
    else:
        return recursiveBinarySearch(arr, target, left, mid-1)

