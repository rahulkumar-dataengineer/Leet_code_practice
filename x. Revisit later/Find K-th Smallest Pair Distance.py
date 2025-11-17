'''

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Need to revisit !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

719. Find K-th Smallest Pair Distance

The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,1,1], k = 2
Output: 0

Example 3:
Input: nums = [1,6,1], k = 3
Output: 5

Constraints:
n == nums.length
2 <= n <= 104
0 <= nums[i] <= 10^6
1 <= k <= n * (n - 1) / 2
'''
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        length = len(nums)
        window_lookup = [0] * (length+1)
        max_pairs = (length * (length-1))/2
        window = 0
        result = []

        for window_size in range(length+1):
            window_lookup[window_size] = (length+1) - window_size

        for index in range(len(window_lookup)):
            if index >= 2:
                if k > window_lookup[index]:
                    k =  k - window_lookup[index]
                else:
                    window = index
                    break

        left = 0
        right = window-1
        while right < length:
            result.append(nums[right] - nums[left])
            left+=1
            right+=1
        
        result.sort()
        return result[k-1]
    


solution = Solution()

nums = [9,10,7,10,6,1,5,4,9,8]
k = 18
print(solution.smallestDistancePair(nums, k)) # Output: 2

nums = [1,3,1]
k = 1
print(solution.smallestDistancePair(nums, k)) # Output: 0

nums = [1,1,1]
k = 2
print(solution.smallestDistancePair(nums, k)) # Output: 0


nums = [1,6,1]
k = 3
print(solution.smallestDistancePair(nums, k)) # Output: 5