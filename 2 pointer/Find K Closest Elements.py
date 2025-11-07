'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Need to revisit !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-104 <= arr[i], x <= 10^4
'''

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-k
        



solution = Solution()
arr = [1,2,3,4,5]
k = 4
x = 3
# Output: [1,2,3,4]
print(solution.findClosestElements(arr, k, x))


arr = [1,1,2,3,4,5]
k = 4
x = -1
# Output: [1,1,2,3]
print(solution.findClosestElements(arr, k, x))

arr = [-2,-1,1,2,3,4,5]
k = 7
x = 3
# [-2,-1,1,2,3,4,5]
print(solution.findClosestElements(arr, k, x))

arr = [0,1,1,1,2,3,6,7,8,9]
k = 9
x = 4
# [0,1,1,1,2,3,6,7,8]
print(solution.findClosestElements(arr, k, x))

arr = [1,1,1,10,10,10]
k = 1
x = 9
# [10]
print(solution.findClosestElements(arr, k, x))

arr = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
# [3,3,4]
print(solution.findClosestElements(arr, k, x))

