'''
1. 2 sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for ii in range(i+1, len(nums)):
        #         if nums[i] + nums[ii] == target:
        #             return [i, ii]

        # result = {}
        # for i in range(len(nums)):
        #     result[nums[i]] = i
        
        # for i in range(len(nums)):
        #     x = target - nums[i]
        #     if x in result and result[x]!=i:
        #         return [i, result[x]]
        # return []

        result = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in result:
                return [i, result[x]]
            result[nums[i]] = i
        return []
            

# Example usage:
solution = Solution()

nums = [1,0,2,3,0,4,6]
target = 0
print(solution.twoSum(nums, target)) # [1,4]

target = 5
print(solution.twoSum(nums, target)) # [2,3]

target = 9
print(solution.twoSum(nums, target)) # [3,6]

target = 11
print(solution.twoSum(nums, target)) # []