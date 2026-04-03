'''
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        left = right = 0
        max_length = 0
        maxf = 0
        seen = {}

        while right < length:
            seen[s[right]] = 1 + seen.get(s[right], 0)
            maxf = max(maxf, seen[s[right]])
            window_len = right - left + 1
            
            while left <= right and (window_len - maxf) > k:
                seen[s[left]] -= 1
                left += 1
                window_len -= 1

            max_length = max(max_length, window_len)
            right += 1
        return max_length
    
solution = Solution()
s = "ABAB"
k = 2
print(solution.characterReplacement(s, k)) # Output: 4


s = "AABABBA"
k = 1
print(solution.characterReplacement(s, k)) # Output: 4
