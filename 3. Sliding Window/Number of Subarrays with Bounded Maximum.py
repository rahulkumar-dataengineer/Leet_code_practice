'''
795. Number of Subarrays with Bounded Maximum

Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Example 2:
Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9
'''
from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        left_boundry = right_boundry = 0
        last_valid = -1   # Track last index where nums[i] is within [left, right]
        count = 0
        length = len(nums)

        while right_boundry < length:
            if nums[right_boundry] > right:
                left_boundry = right_boundry = right_boundry + 1
                last_valid = -1  # reset; not possible to form valid subarray
                continue
            if left <= nums[right_boundry] <= right:
                last_valid = right_boundry
            if last_valid != -1:
                count += last_valid - left_boundry + 1
            right_boundry += 1

        return count


solution = Solution()

nums = [2,1,4,3]
left = 2
right = 3
print(solution.numSubarrayBoundedMax(nums, left, right))# Output: 3

nums = [2,9,2,5,6]
left = 2
right = 8
print(solution.numSubarrayBoundedMax(nums, left, right))# Output: 7

nums = [73,55,36,5,55,14,9,7,72,52]
left = 32
right = 69
print(solution.numSubarrayBoundedMax(nums, left, right))# Output: 22

        