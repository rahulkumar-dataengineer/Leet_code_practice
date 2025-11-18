'''
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:
1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length
'''
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        length = len(fruits)
        left = right = 0
        max_length = 0
        distinct = 0
        seen = {}

        while right < length:

            if fruits[right] in seen:
                seen[fruits[right]] += 1
            else:
                seen[fruits[right]] = 1
                distinct += 1
            
            if distinct > 2:
                seen[fruits[left]] -= 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                    distinct -= 1
                left += 1
            
            max_length = max(right - left + 1, max_length)
            right += 1
        
        return max_length


solution = Solution()

fruits = [1,2,1]
print(solution.totalFruit( fruits)) #3

fruits = [0,1,2,2]
print(solution.totalFruit( fruits)) #3

fruits = [1,2,3,2,2]
print(solution.totalFruit( fruits)) #4