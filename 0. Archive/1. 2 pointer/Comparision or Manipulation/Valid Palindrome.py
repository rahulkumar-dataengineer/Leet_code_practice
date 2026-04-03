'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
'''

class Solution:
    def isAlphaNumeric(self, character):
        return (
            ord("A") <= ord(character) <= ord("Z") or
            ord("a") <= ord(character) <= ord("z") or
            ord("0") <= ord(character) <= ord("9")
        )
            

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<right:
            while left < right and not self.isAlphaNumeric(s[left]):
                left+=1
            
            while left < right and not self.isAlphaNumeric(s[right]):
                right-=1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left+=1
            right-=1

        return True
    

solution = Solution()

s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s), "\t", s)

s = "race a car"
print(solution.isPalindrome(s), "\t", s)

s = " "
print(solution.isPalindrome(s), "\t", s)



        