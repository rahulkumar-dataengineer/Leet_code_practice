'''
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 
Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:
1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
'''

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        length = len(intervals)
        count = 0
        start = 0
        end = 1
        index = 1
        result = []
        previous = intervals[0]

        while index < length:
            if  previous[end] <= intervals[index][start]:
                result.append(previous)
                previous = intervals[index]

            else:
                if previous[end] > intervals[index][end]:
                    result.append(intervals[index])
                    previous = intervals[index]

                count += 1
            
            index += 1
        
        result.append(previous)
            
        
        print(result)
        return count



solution = Solution()

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(solution.eraseOverlapIntervals(intervals)) # Output: 1

intervals = [[1,2],[1,2],[1,2]]
print(solution.eraseOverlapIntervals(intervals)) # Output: 2

intervals = [[1,2],[2,3]]
print(solution.eraseOverlapIntervals(intervals)) # Output: 0

intervals = [[1,2], [3,4], [5,6], [5,7], [6,8], [4,9], [8,9]]
print(solution.eraseOverlapIntervals(intervals)) # Output: 2

intervals = [[1,2],[1,3],[1,4]]
print(solution.eraseOverlapIntervals(intervals)) # Output: 2