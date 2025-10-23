'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.


Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums [2]

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            left_index = i+1
            right_index = len(nums)-1

            while left_index < right_index:
                total = nums[i] + nums[left_index] + nums[right_index]

                if abs(target - total) < abs(target - closest_sum):
                    closest_sum = total

                if total<target:
                    left_index+=1
                elif total>target:
                    right_index-=1
                else:
                    return total
        
        return closest_sum



solution = Solution()

nums = [-1,2,1,-4]
target = 1 #2
print(nums, "\t",solution.threeSumClosest(nums, target))

nums = [0,0,0]
target = 1 # 0
print(nums, "\t",solution.threeSumClosest(nums, target))

nums = [10,20,30,40,50,60,70,80,90]
target = 1 #60
print(nums, "\t",solution.threeSumClosest(nums, target))