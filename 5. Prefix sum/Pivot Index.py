'''
1991.  Find the Middle Index in Array
724. Find pivot index

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

Example 1:
Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4

Example 2:
Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0

Example 3:
Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.
 

Constraints:
1 <= nums.length <= 100
-1000 <= nums[i] <= 1000
'''
from typing import List

class Solution:
    def findMiddleIndex1(self, nums: List[int]) -> int:
        length = len(nums)
        lsum = [0] * length
        rsum = [0] * length

        lsum[0] = nums[0]
        for index in range(1, length):
            lsum[index] = lsum[index - 1] + nums[index]
        
        rsum[-1] = nums[-1]
        for index in range(length - 2, -1, -1):
            rsum[index] = rsum[index + 1] + nums[index]

        for index in range(length):
            if rsum[index] == lsum[index]:
                return index
        return -1
        
    
    '''
    total = lsum + value + rsum, rearranging this rsum = total - value - lsum
    for each index compare the lsum == rusm, if not move to next index
    '''    
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0

        for index, value in enumerate(nums):
            rsum = total - lsum - value
            if lsum == rsum:
                return index
            lsum += value
        
        return -1



solution = Solution()

nums = [
    [2,3,-1,8,4],
    [1,-1,4],
    [2,5]
]

for num in nums:
    print(solution.findMiddleIndex(num))