'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2 

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
'''

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        prefix = 0
        count = 0

        for element in nums:
            prefix += element
            valid_subarray = prefix - k
            if valid_subarray in prefix_map:
                count += prefix_map[valid_subarray]
            
            prefix_map[prefix] = 1 + prefix_map.get(prefix, 0)
        
        return count



solution = Solution()

nums = [
    [1,1,1],
    [1,2,3]
]

k = [2, 3]

for index in range(len(nums)):
    print(solution.subarraySum(nums[index], k[index]))