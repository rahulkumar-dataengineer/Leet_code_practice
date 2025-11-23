'''
759. Employee Free Time
https://algo.monster/liteproblems/759

Given a list of employee work schedules with each employee having a list of non-overlapping intervals representing their working hours, we are tasked with finding the common free time for all employees, or in other words, the times when all employees are not working.

The input is a nested list of intervals, each interval as [start, end], with start < end. The intervals are non-overlapping and are already sorted in ascending order. The output should also be a list of sorted intervals.

For example, consider 
schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]].
output = [[5,6], [7,9]]

Here, Employee 1 works from 1 to 3 and 6 to 7. Employee 2 works from 2 to 4 and Employee 3 works from 2 to 5 and 9 to 12. The common free time for all employees is [5,6] and [7,9] as these are the intervals when all employees are free.

'''

from typing import List

'''
time = O(N + M)
space = O(M)

when M ~ N then this is ideal solution
'''

class Solution:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        start = 0
        end = 1
        result = []
        max_end = 0

        for emp_schedule in schedule:
            for slots in emp_schedule:
                _, end_time = slots
                max_end = max(max_end, end_time)
        
        prefix_arr = [0] * (max_end + 1)
        
        for emp_schedule in schedule:
            for slots in emp_schedule:
                start_time, end_time = slots
                prefix_arr[start_time] += 1
                prefix_arr[end_time] -= 1
        
        interval_start = None

        for index in range(1, max_end+1):
            prefix_arr[index] += prefix_arr[index - 1]
            if prefix_arr[index] == 0 and not interval_start:
                interval_start = index
                continue
            if prefix_arr[index] == 1 and interval_start:
                result.append([interval_start, index])
                interval_start = None
        
        return result


'''
time = O(N LogN)
space = O(N)

when M >> N then this is ideal solution
- flatten the array and sort
- merge the intervals
- find the gap
'''
class Solution2:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        start = 0
        end = 1
        result = []
        intervals = [slots for emp_schedule in schedule for slots in emp_schedule]

        intervals.sort(key = lambda x: x[0])
        length = len(intervals)

        curr = intervals[0]
        
        for index in range(1, length):
            if curr[end] < intervals[index][start]:
                result.append(curr)
                curr = intervals[index]
            
            elif curr[start] > intervals[index][end]:
                result.append(intervals[index])
            else:
                curr = [
                    min(intervals[index][start], curr[start]),
                    max(intervals[index][end], curr[end])
                ]
        result.append(curr)
        
        free_time = []
        for index in range(1, len(result)):
            free_time.append([result[index - 1][end], result[index][start]])
        
        return free_time



solution = Solution()
solution2 = Solution2()

schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
print(solution.employeeFreeTime(schedule)) #[[5,6], [7,9]]
print(solution2.employeeFreeTime(schedule)) #[[5,6], [7,9]]