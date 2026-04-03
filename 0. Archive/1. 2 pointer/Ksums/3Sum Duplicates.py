'''
923. 3Sum With Multiplicity

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.


Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Example 3:
Input: arr = [2,1,3], target = 6
Output: 1
Explanation: (1, 2, 3) occured one time in the array so we return 1.
 

Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
'''
from typing import List

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        length = len(arr)
        count = 0

        for index1 in range(length-2):
            left = index1+1
            right = length-1

            while left<right:
                sum = arr[index1] + arr[left] + arr[right]
                if sum > target:
                    right-=1
                elif sum < target:
                    left+=1
                else:
                    if arr[left]!=arr[right]:
                        left_count, right_count = 1,1
                        while left<right and arr[left] == arr[left+1]:
                            left+=1
                            left_count+=1
                        while left<right and arr[right] == arr[right-1]:
                            right-=1
                            right_count+=1
                        count += left_count * right_count
                        left+=1
                        right-=1
                    else:
                        total = right-left+1
                        count += total*(total-1)//2
                        break
        
        return count%(10**9+7)
        
    




solution = Solution()

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
print(arr, "\t",solution.threeSumMulti(arr,target))  #20

arr = [1,1,2,2,2,2]
target = 5
print(arr, "\t",solution.threeSumMulti(arr, target)) #12

arr = [2,1,3]
target = 6
print(arr, "\t",solution.threeSumMulti(arr, target)) #1


