'''
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s2)
        window = len(s1)
        left = 0
        right = window
        count_s1 = {}
        count_s2 = {}

        if window > length:
            return False

        for index in range(window):
            count_s1[s1[index]] = 1 + count_s1.get(s1[index], 0)
            count_s2[s2[index]] = 1 + count_s2.get(s2[index], 0)
        
        if count_s1 == count_s2:
                return True
        
        while right < length:
            count_s2[s2[right]] = 1 + count_s2.get(s2[right], 0)
            count_s2[s2[left]] -= 1
            if count_s2[s2[left]] == 0:
                del count_s2[s2[left]]

            if count_s1 == count_s2:
                return True
            
            left += 1
            right += 1
        
        return False


solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2)) # Output: true



s1 = "ab"
s2 = "eidboaoo"
print(solution.checkInclusion(s1, s2)) # Output: False
