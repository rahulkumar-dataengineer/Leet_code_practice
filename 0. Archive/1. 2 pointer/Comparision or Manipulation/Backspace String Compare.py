'''
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
 
Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
'''


'''
This solution takes O(N+M) or O(N) time but takes O(N+M) space too. 
That is because I am using join to create a new string. 
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def modify(sentence):
            pointer = len(sentence)-1
            count = 0
            while pointer>=0:
                if sentence[pointer] == '#':
                    count+=1
                else:
                    if count>0:
                        sentence[pointer] = '#'
                        count-=1
                pointer-=1
            return sentence
    
        def removeHash(sentence):
            sentence = ''.join([value for value in sentence if value!='#'])
            return sentence
    
        s = removeHash(modify(list(s)))
        t = removeHash(modify(list(t)))
        print(s)
        print(t)
        return s == t
    
    
'''
Another solution to do in O(1) space. 

Instead of modifying the complete string, what if we just compare the indexes of both the strings. we just need a way to find the valid index to compare.

I can modify the 'modify' function to just stop and retrun the index instead of processing it completely.
Then use the index to compare the 2 strings at same index.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getValidIndex(string, start):
            countBackspace = 0
            index = start

            while index>=0:
                if string[index] == '#':
                    countBackspace+=1
                    index-=1
                else:
                    if countBackspace>0:
                        countBackspace-=1
                        index-=1
                    else:
                        break
            return index
        
        index_s = len(s)-1
        index_t = len(t)-1

        while index_s>=0 or index_t>=0:
            index_s = getValidIndex(s,index_s)
            index_t = getValidIndex(t,index_t)

            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""
            
            if char_s != char_t:
                return False
            index_s-=1
            index_t-=1
        return True




solution = Solution()

s = "ab#c"
t = "ad#c"
print(f"{s} and {t} are same", solution.backspaceCompare(s, t)) # true

s = "ab##"
t = "c#d#"
print(f"{s} and {t} are same", solution.backspaceCompare(s, t)) # true

s = "a#c"
t = "b"
print(f"{s} and {t} are same", solution.backspaceCompare(s, t)) # false

s = "a##c"
t = "#a#c"
print(f"{s} and {t} are same", solution.backspaceCompare(s, t)) # true

s= "xywrrmp"
t = "xywrrmu#p"
print(f"{s} and {t} are same", solution.backspaceCompare(s, t)) # true