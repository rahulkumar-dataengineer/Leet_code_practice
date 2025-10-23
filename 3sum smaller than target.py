'''
https://www.lintcode.com/problem/3sum-smaller/description

918. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example1
Input:  nums = [-2,0,1,3], target = 2
Output: 2
Explanation:
Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]


Example2
Input: nums = [-2,0,-1,3], target = 2
Output: 3
Explanation:
Because there are three triplets which sums are less than 2:
[-2, 0, -1]
[-2, 0, 3]
[-2, -1, 3]
'''

from typing import (
    List,
)

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums)):

            left_index = i+1
            right_index = len(nums)-1

            while left_index < right_index:
                total = nums[i] + nums[left_index] + nums[right_index]

                if total<target:
                    count+=right_index-left_index # This is the trick, here when array is sorted, if i+left_index+right_index < target. then any value between left and right index will also satisfy this.
                    left_index+=1
                else:
                    right_index-=1
        
        return count
    


solution = Solution()

nums = [-2,0,1,3]
target = 2 # Output: 2
print(nums, "\t",solution.three_sum_smaller(nums, target))


nums = [-2,0,-1,3]
target = 2 # Output: 3
print(nums, "\t",solution.three_sum_smaller(nums, target))