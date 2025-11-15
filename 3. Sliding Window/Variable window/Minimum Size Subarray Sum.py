'''
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
 
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        left = right = 0
        total = 0
        min_window = float("inf")

        while left<=right and right < length:
            total += nums[right]
            while total >= target:
                min_window = min (right - left + 1, min_window)
                total -= nums[left]
                left+=1
            right+=1
        return 0 if min_window ==float("inf") else min_window





solution = Solution()

target = 7 
nums = [2,3,1,2,4,3]
print(solution.minSubArrayLen(target, nums))  #Output: 2

target = 4
nums = [1,4,4]
print(solution.minSubArrayLen(target, nums))  #Output: 1


target = 11 
nums = [1,1,1,1,1,1,1,1]
print(solution.minSubArrayLen(target, nums))  #Output: 0

target = 11 
nums = [1,2,3,4,5]
print(solution.minSubArrayLen(target, nums))  #Output: 3
        