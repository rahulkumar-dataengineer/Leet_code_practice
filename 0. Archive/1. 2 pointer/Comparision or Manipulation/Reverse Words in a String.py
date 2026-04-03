'''
151. Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 10^4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

'''


class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        length = len(s)

        left, right = length-1, length-1

        while left>=0:
            while left>=0 and s[left] == ' ':
                left-=1
                right-=1
            while left>=0 and s[left] != ' ':
                left-=1
            
            if s[left+1] != " ":
                result.append(s[left+1:right+1])
                result.append(' ')
            right = left-1
            left-=1      
        return "".join(result[:-1])




solution = Solution()

s = "the sky is blue"
# Output: "blue is sky the"
print(solution.reverseWords(s))

s = "  hello world  "
# Output: "world hello"
print(solution.reverseWords(s))


s = "a good   example"
# Output: "example good a"
print(solution.reverseWords(s))

s = "   fffff ff gg ee"
# "ee gg ff fffff"
print(solution.reverseWords(s))