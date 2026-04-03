'''
713. Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


Example 2:
Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:
1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
'''

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left_pointer = 0
        right_pointer = 0
        count = 0
        product = 1

        if k <= 1:
            return 0

        while right_pointer < len(nums):
            product *= nums[right_pointer]
            while product >= k:
                product //= nums[left_pointer]
                left_pointer+=1
            count += right_pointer - left_pointer + 1
            right_pointer+=1
        
        return count

                
solution = Solution()
nums = [10,5,2,6] 
k = 100
print(solution.numSubarrayProductLessThanK(nums, k)) # Output: 8


nums = [1,2,3]
k = 0
print(solution.numSubarrayProductLessThanK(nums, k)) # Output: 0




        