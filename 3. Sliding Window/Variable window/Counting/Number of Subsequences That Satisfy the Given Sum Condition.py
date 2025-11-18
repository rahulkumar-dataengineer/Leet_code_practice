'''
1498. Number of Subsequences That Satisfy the Given Sum Condition

You are given an array of integers nums and an integer target.
Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 10^9 + 7.

 
Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
 

Constraints:

1 <= nums.length <= 10**5
1 <= nums[i] <= 10**6
1 <= target <= 10**6
'''

'''
what I learned

- Subsequence - array of elements which are in order but not continious (like subarray)
- how to calculate total number of subsequence - 2^N, where N is total number of elements, but that includes empty subsequence too (1 subsequence). If it should have atleast 1 element always, then 2^(N-1).

- precomputing powers is always a good idea as I can mod the result when calculating. else if i calculate the power everytime,  we 1st get the value and then mode, if this value is large enough it can cause problem. 
'''
from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        preComputePower = [1]*length
        mod = 10**9 + 7
        totalSubsequence = 0

        for index in range(1, length):
            preComputePower[index] = (preComputePower[index-1] * 2) % mod

        left_index = 0
        right_index = length-1

        while left_index<=right_index:
            sum = nums[left_index]+nums[right_index]

            if sum>target:
                right_index-=1
            else:
                totalSubsequence = (totalSubsequence + preComputePower[right_index-left_index]) % mod
                left_index+=1
        
        return totalSubsequence


solution = Solution()

nums = [3,5,6,7]
target = 9
print(solution.numSubseq(nums, target)) # Output: 4

nums = [3,3,6,8]
target = 10
print(solution.numSubseq(nums, target)) # Output: 6

nums = [2,3,3,4,6,7]
target = 12
print(solution.numSubseq(nums, target)) # Output: 61
        