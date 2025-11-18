'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        left = right = 0
        max_length = 0
        seen = {}
        
        while right < length:
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1

            while left <= right and seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
            max_length = max(right - left + 1, max_length)
            right += 1
        return max_length
        

solution = Solution()

s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s)) #3

s = "bbbbb"
print(solution.lengthOfLongestSubstring(s)) #1

s = "pwwkew"
print(solution.lengthOfLongestSubstring(s)) #3
