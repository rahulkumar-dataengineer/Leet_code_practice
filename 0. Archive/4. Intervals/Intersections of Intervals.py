'''
986. Interval List Intersections

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 10^9
endi < starti+1
0 <= startj < endj <= 10^9 
endj < startj+1
'''

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f_length = len(firstList)
        s_length = len(secondList)

        start = 0
        end = 1

        if not firstList or not secondList:
            return []

        output=[]

        f_index,s_index = 0,0

        while f_index < f_length and s_index < s_length:
            
            inter_start = max(firstList[f_index][start],secondList[s_index][start])
            inter_end = min(firstList[f_index][end],secondList[s_index][end])

            if inter_start <= inter_end:
                output.append([inter_start,inter_end])

            if firstList[f_index][end] <= secondList[s_index][end]:
                f_index+=1
            else:
                s_index+=1
        
        return output



solution = Solution()
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(solution.intervalIntersection(firstList, secondList)) # Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


firstList = [[1,3],[5,9]]
secondList = []
print(solution.intervalIntersection(firstList, secondList)) # Output: []