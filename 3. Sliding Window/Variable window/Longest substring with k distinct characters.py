'''
longest substring with k distinct characters

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more 
than '2' distinct characters is "araa".


Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more 
than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more 
than '3' distinct characters are "cbbeb" & "bbebi".
'''

class Solution:
    def maxSubArrayLen(self, k: int, s: str) -> int:
        length = len(s)
        left = right = 0
        max_length = 0
        distinct_chars = 0
        seen = {}
        
        while right < length:
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
                distinct_chars += 1
            
            if distinct_chars > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    distinct_chars -= 1
                    del seen[s[left]]
                left+=1
            
            max_length = max(right - left + 1, max_length)
            right+=1
        return max_length




solution = Solution()

k = 2
s = "araaci"
print(solution.maxSubArrayLen(k, s))  #Output: 4

k = 1
s = "araaci"
print(solution.maxSubArrayLen(k, s))  #Output: 2


k = 3
s = "cbbebi"
print(solution.maxSubArrayLen(k, s))  #Output: 5

k = 0
s = ""
print(solution.maxSubArrayLen(k, s))  #Output: 0

k = 1
s = "ab"
print(solution.maxSubArrayLen(k, s))  #Output: 1

k = 2
s = "ab"
print(solution.maxSubArrayLen(k, s))  #Output: 2

k = 3
s = "aabacbebebe"
print(solution.maxSubArrayLen(k, s))  #Output: 7

k = 2
s = "aabacbebebe"
print(solution.maxSubArrayLen(k, s))  #Output: 6

k = 2
s = "abccdef"
print(solution.maxSubArrayLen(k, s))  #Output: 3

k = 1
s = "aabbc"
print(solution.maxSubArrayLen(k, s))  #Output: 2