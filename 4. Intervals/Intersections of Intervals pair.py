'''
Check if any two intervals intersect
https://www.geeksforgeeks.org/dsa/check-if-any-two-intervals-overlap-among-a-given-set-of-intervals/


Input:  arr[] = [[1, 3], [5, 7], [2, 4], [6, 8]]
Output: True
Explanation: The intervals {1, 3} and {2, 4} overlap

Input:  arr[] = [[1, 3], [7, 9], [4, 6], [10, 13]]
Output: False
Explanation: No pair of intervals overlap. 
'''

from typing import List


'''
the usual sorting and comparing will take O(n log n) time and O(1) space.
we want to reduce the time complexity - use prefix sum

if they touch - they intersect, that is the reason we extend end by 1
'''
class Solution:
    def isIntersect(self, intervals: List[List[int]]) -> bool:
        
        max_length = 0
        for _, int_end in intervals:
            max_length = max(max_length, int_end)
        
        prefix_sum = [0] * (max_length + 2)

        for int_start, int_end in intervals:
            prefix_sum[int_start] += 1
            prefix_sum[int_end + 1] -= 1
        

        for index in range(1, len(prefix_sum)):
            prefix_sum[index] += prefix_sum[index - 1]
            if prefix_sum[index] > 1:
                return True
        
        return False



solution = Solution()
intervals = [[1, 3], [5, 7], [2, 4], [6, 8]]
print(solution.isIntersect(intervals)) # Output: True


intervals = [[1, 3], [7, 9], [4, 6], [10, 13]]
print(solution.isIntersect(intervals)) # Output: False

intervals = [[1, 2], [2, 4], [7, 8], [4, 5]]
print(solution.isIntersect(intervals)) # Output: True