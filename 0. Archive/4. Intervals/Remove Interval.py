'''
1272. Remove Interval

A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form (a, b). A real number x is in the set if one of its intervals (a, b) contains x (i.e. a<=x<b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] - [ai, bi] represents the interval [ai, bi) . You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.


Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]



Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]



Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
'''

from typing import List

class Solution:
    def remove(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        length = len(intervals)
        start = 0
        end = 1
        output = []

        if length == 0:
            return output

        for index in range(length):
            # Does not overlap
            if intervals[index][end] < toBeRemoved[start] or intervals[index][start] > toBeRemoved[end]:
                output.append(intervals[index])
            
            else:
                # Completely within
                if toBeRemoved[start] <= intervals[index][start] <= intervals[index][end] <= toBeRemoved[end]:
                    continue
                
                # overlapping on right
                if toBeRemoved[start] > intervals[index][start]:
                    output.append([intervals[index][start], toBeRemoved[start]])
                
                # overlapping on left
                if toBeRemoved[end] < intervals[index][end]:
                    output.append([toBeRemoved[end], intervals[index][end]])


        return output


solution = Solution()
intervals = [[0,2],[3,4],[5,7]]
toBeRemoved = [1,6]
print(solution.remove(intervals, toBeRemoved)) # Output: [[0,1],[6,7]]



intervals = [[0,5], [8,10]]
toBeRemoved = [2,3]
print(solution.remove(intervals, toBeRemoved)) # Output: [[0,2],[3,5],[8,10]]



intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]]
toBeRemoved = [-1,4]
print(solution.remove(intervals, toBeRemoved)) # Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
