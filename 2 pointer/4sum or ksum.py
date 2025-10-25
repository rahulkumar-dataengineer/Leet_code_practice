'''
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        temp = []

        def ksum(k, start, target):
            if k==2:
                twoSum(start, target)
                return
            
            stop = len(nums)-k+1
            
            for outer_element_index, outer_element in enumerate(nums[start:stop], start):
                if outer_element_index>start and outer_element == nums[outer_element_index-1]:
                    continue
                temp.append(outer_element)
                ksum(k-1, outer_element_index+1, target-outer_element)
                temp.pop()

        def twoSum(start, target):
            left_index = start
            right_index = len(nums)-1

            while left_index < right_index:
                total = nums[left_index] + nums[right_index]
                if total>target:
                    right_index-=1
                elif total<target:
                    left_index+=1
                else:
                    result.append(temp + [nums[left_index], nums[right_index]])
                    right_index-=1
                    left_index+=1
                    while left_index < right_index and nums[left_index] == nums[left_index-1]:
                        left_index+=1
                    while left_index < right_index and nums[right_index] == nums[right_index+1]:
                        right_index-=1

        ksum(4, 0, target)
        return result

       



solution = Solution()

nums = [1,0,-1,0,-2,2]
target = 0
print(solution.fourSum(nums, target)) # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums = [2,2,2,2,2]
target = 8
print(solution.fourSum(nums, target)) # Output: [[2,2,2,2]]

nums = [0,0,0,0]
target = 0
print(solution.fourSum(nums, target)) # Output: [[0,0,0,0]]