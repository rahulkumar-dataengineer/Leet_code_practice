'''
556. Next Greater Element III

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.


Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 2^31 - 1
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        left = length-2
        right=length-1

        while left>=0 and digits[left]>=digits[left+1]:
            left-=1
        
        if left<0:
            return -1
        
        while right>left and digits[right]<=digits[left]:
            right-=1
        
        digits[left], digits[right] = digits[right], digits[left]

        digits[left+1:] = sorted(digits[left+1:])

        min_value = int("".join(digits))
        return min_value if min_value < (1<<31) else -1 


solution = Solution()
n = 12
print(n, "\t", solution.nextGreaterElement(n)) # Output: 21

n = 21
print(n, "\t", solution.nextGreaterElement(n)) # Output: -1