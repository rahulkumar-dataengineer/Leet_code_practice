'''
30. Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]

Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.



Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Explanation:
There is no concatenated substring.



Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:
1 <= s.length <= 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
'''

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(s)
        window_len = len(words[0])
        count_w = {}

        for word in words:
            count_w[word] = 1 + count_w.get(word, 0)

        result = []
        
        left = 0
        right = window_len

        count_s = {}
        count_w = {}

        

        have = 0
        need = len(count_w)

        for character in count_w:
            if count_s[character] == count_w[character]:
                have += 1

        
        while right < length:
            if have == need:
                result.append(left)
            
            count_s[s[right]] = 1 + count_s.get(s[right], 0)
            count_s[s[left]] -= 1

            if s[left] in count_w and count_s[s[left]] < count_w[s[left]]:
                have -= 1

            if s[right] in count_w and count_s[s[right]] == count_w[s[right]]:
                have += 1

            
            right += 1
            left += 1
            
        
        return result


solution = Solution()

s = "barfoothefoobarman"
words = ["foo","bar"]
print(solution.findSubstring(s, words)) # Output: [0,9]


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(solution.findSubstring(s, words)) # Output: []


s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(solution.findSubstring(s, words)) # Output: [6,9,12]