'''
1288. Remove Covered Intervals

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.


Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:
Input: intervals = [[1,4],[2,3]]
Output: 1
 
Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 10^5
All the given intervals are unique.
'''

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        start = 0
        end = 1
        length = len(intervals)
        count = length

        intervals.sort(key = lambda x: x[start])

        prev = intervals[0]

        for index in range(1, length):
            curr = intervals[index]

            inter_start = max(prev[start], curr[start])
            inter_end = min(prev[end], curr[end])

            if inter_start <= inter_end:
                if [inter_start, inter_end] == curr:
                    count -= 1
                elif [inter_start, inter_end] == prev:
                    count -= 1
                    prev = curr
                else:
                    prev = curr
        return count


'''another more elegant solution'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        start = 0
        end = 1
        length = len(intervals)
        count = 1

        intervals.sort(key = lambda x: (x[start], -x[end]))

        prev = intervals[0]

        for index in range(1, length):
            curr = intervals[index]

            if prev[start] <= curr[start] and prev[end] >= curr[end]:
                continue
            prev = curr
            count += 1
        return count



solution = Solution()
intervals = [
    [[1, 4], [3, 6], [2, 8]],
    [[1, 4], [2, 3]],
    [[1, 2], [1, 4], [3, 4]],
    [[66672,75156],[59890,65654],[92950,95965],[9103,31953],[54869,69855],[33272,92693],[52631,65356],[43332,89722],[4218,57729],[20993,92876]]
]

for interval in intervals:
    print(solution.removeCoveredIntervals(interval))