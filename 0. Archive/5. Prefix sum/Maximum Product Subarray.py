'''
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        maxi = float('-inf')
        prefix = 1
        postfix = 1

        for index in range(length):
            if prefix == 0:
                prefix = 1
            
            if postfix == 0:
                postfix = 1
            
            prefix *= nums[index]
            postfix *= nums[length - index - 1]

            maxi = max(maxi, max(prefix, postfix))
        
        return maxi
        
        


solution = Solution()

numss = [
    [2,3,-2,4],
    [-2,0,-1],
    [-2]
]

for nums in numss:
    print(solution.maxProduct(nums))