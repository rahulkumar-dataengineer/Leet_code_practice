'''
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.


Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        length = len(intervals)
        output = []
        start = 0
        end = 1

        if length == 0:
            return output

        curr = intervals[0]
        
        for index in range(1, length):
            if curr[end] < intervals[index][start]:
                output.append(curr)
                curr = intervals[index]
            
            elif curr[start] > intervals[index][end]:
                output.append(intervals[index])
            else:
                curr = [
                    min(intervals[index][start], curr[start]),
                    max(intervals[index][end], curr[end])
                ]
        output.append(curr)
        return output



solution = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution.merge(intervals)) # Output: [[1,6],[8,10],[15,18]]


intervals = [[1,4],[4,5]]
print(solution.merge(intervals)) # Output: [[1,5]]

intervals = [[4,7],[1,4]]
print(solution.merge(intervals)) # Output: [[1,7]]


