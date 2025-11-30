'''
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30

The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length
        
        for index in range(1, length):
            left[index] = left[index - 1] * num[index - 1]
        
        for index in range(length-2, -1, -1):
            right[index] = right[index + 1] * num[index + 1]
        
        for index in range(length):
            nums[index] = left[index] * right[index]
        
        return nums

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        prefix = 1
        postfix = 1

        for index in range(len(nums)):
            output[index] = prefix
            prefix *= nums[index]

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        




solution = Solution()

nums = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]

for num in nums:
    print(solution.productExceptSelf(num))


