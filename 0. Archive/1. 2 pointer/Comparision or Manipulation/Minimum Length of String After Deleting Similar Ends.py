'''
1750. Minimum Length of String After Deleting Similar Ends

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

Example 1:
Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.

Example 2:
Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:
Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 

Constraints:
1 <= s.length <= 10^5
s only consists of characters 'a', 'b', and 'c'.
'''

class Solution:
    def minimumLength(self, s: str) -> int:
        length = len(s)
        total_length = length
        left = 0
        right = length-1

        while left<right:
            if s[left] != s[right]:
                return total_length
            while left<right and s[left] == s[left+1]:
                left+=1
            while left<right and s[right] == s[right-1] and s[right]==s[left]:
                right-=1
            total_length -= (left+1) + (total_length-right)
            left+=1
            right-=1
        
        if total_length<0:
            return 0
        return total_length
    



solution = Solution()

s = "ca"
# Output: 2
print(solution.minimumLength(s))

s = "cabaabac"
# Output: 0
print(solution.minimumLength(s))

s = "aabccabba"
# Output: 3
print(solution.minimumLength(s))
