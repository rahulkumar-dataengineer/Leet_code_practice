'''
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

class Solution:
    def checkValidity(self, count_s, count_t):
            for key in count_t.keys():
                if count_s.get(key, 0) < count_t[key]:
                    return False
            return True


    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        window = len(t)
        min_length = ""

        left = 0
        right = window

        count_s = {}
        count_t = {}

        if window > length:
            return min_length

        for index in range(window):
            count_s[s[index]] = 1 + count_s.get(s[index], 0)
            count_t[t[index]] = 1 + count_t.get(t[index], 0)

        if self.checkValidity(count_s, count_t):
            min_length = s[left:right]
            
        
        while right < length:
            count_s[s[right]] = 1 + count_s.get(s[right], 0)

            while left <= right and self.checkValidity(count_s, count_t):
                candidate = s[left:right+1]
                if not min_length or len(candidate) < len(min_length):
                    min_length = candidate
                count_s[s[left]] -= 1
                if count_s[s[left]] == 0:
                    del count_s[s[left]]
                left += 1
            right += 1
        
        return min_length



solution = Solution()

s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t)) # Output: "BANC"

s = "a"
t = "a"
print(solution.minWindow(s, t)) # Output: "a"

s = "a"
t = "aa"
print(solution.minWindow(s, t)) # Output: ""

s = "ab"
t = "A"
print(solution.minWindow(s, t)) # Output: "a"

s = "ab"
t = "b"
print(solution.minWindow(s, t)) # Output: "b"

s = "abc"
t = "cba"
print(solution.minWindow(s, t)) # Output: "abc"

s = "bbaa"
t = "aba"
print(solution.minWindow(s, t)) # Output: "baa"

s = "acbbaca"
t = "aba"
print(solution.minWindow(s, t)) # Output: "baca"