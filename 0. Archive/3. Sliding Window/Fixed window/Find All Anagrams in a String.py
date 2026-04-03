'''
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
'''

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(s)
        window = len(p)
        left = 0
        right = window
        
        result = []
        count_s = {}
        count_p = {}

        if window > length:
            return []

        for index in range(window):
            count_s[s[index]] = 1 + count_s.get(s[index], 0)        
            count_p[p[index]] = 1 + count_p.get(p[index], 0)
        
        if count_s == count_p:
            result.append(0)
        
        while right < length:
            count_s[s[right]] = 1 + count_s.get(s[right], 0)
            count_s[s[left]] -= 1
            if count_s[s[left]] == 0:
                del count_s[s[left]]
            
            if count_s == count_p:
                result.append(left+1)
            
            left += 1
            right += 1
        
        return result

solution = Solution()

s = "cbaebabacd"
p = "abc"
print(solution.findAnagrams(s, p)) # Output: [0,6]


s = "abab"
p = "ab"
print(solution.findAnagrams(s, p)) # Output: [0,1,2]