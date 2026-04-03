'''
633. Sum of Square Numbers

Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:
Input: c = 3
Output: false

Constraints:

0 <= c <= 2^31 - 1
'''

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        last_index = int(c ** 0.5)
        
        left = 0
        right = last_index

        while left <= right:
            sum = left**2 + right**2
            if sum < c:
                left+=1
            elif sum > c:
                right-=1
            else:
                return True
        return False




solution = Solution()

c = 5
print(solution.judgeSquareSum(c)) # Output: true

c = 3
print(solution.judgeSquareSum(c)) # Output: false

c = 10000
print(solution.judgeSquareSum(c)) # Output: true

