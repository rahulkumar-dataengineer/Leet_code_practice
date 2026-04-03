'''
57. Insert Intervals

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]. 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5

intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
'''

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        output = []
        start = 0
        end = 1

        if length == 0:
            return output

        curr = newInterval
        
        for index in range(length):
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
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(solution.insert(intervals, newInterval)) # Output: [[1,5],[6,9]]

 

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(solution.insert(intervals, newInterval)) # Output: [[1,2],[3,10],[12,16]]