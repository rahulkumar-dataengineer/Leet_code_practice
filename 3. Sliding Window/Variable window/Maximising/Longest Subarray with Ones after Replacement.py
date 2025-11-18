'''
1004. Longest Subarray with Ones after Replacement
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums =[1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums =[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left = right = 0
        max_length = 0
        zero_count = 0

        while right < length:
            if nums[right] == 0:
                zero_count += 1
            while left <= right and zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length



solution = Solution()

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(solution.longestOnes(nums, k)) # Output: 6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(solution.longestOnes(nums, k)) # Output: 10