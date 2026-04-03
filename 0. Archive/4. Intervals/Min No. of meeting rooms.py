'''
Meeting rooms - Find minimum meeting rooms
https://www.geeksforgeeks.org/dsa/meeting-rooms-find-minimum-meeting-rooms/

Task is to find minimum number of rooms required to attend all meetings.
Note: A person can also attend a meeting if it's starting time is same as the previous meeting's ending time.
'''

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> bool:
        max_length = 0
        count = 1
        for _, int_end in intervals:
            max_length = max(max_length, int_end)
        
        prefix_sum = [0] * (max_length + 1)

        for int_start, int_end in intervals:
            prefix_sum[int_start] += 1
            prefix_sum[int_end] -= 1
        

        for index in range(1, len(prefix_sum)):
            prefix_sum[index] += prefix_sum[index - 1]
            if prefix_sum[index] > 1:
                count = max(count, prefix_sum[index])
        
        return count



solution = Solution()
intervals = [[1, 4], [10, 15], [7, 10]]
print(solution.minMeetingRooms(intervals)) # Output: 1


intervals = [[2, 4], [9, 12], [6, 10]]
print(solution.minMeetingRooms(intervals)) # Output: 2


intervals = [[1, 3], [5, 7], [2, 4], [6, 8]]
print(solution.minMeetingRooms(intervals)) # Output: 2


intervals = [[1, 3], [7, 9], [4, 6], [10, 13]]
print(solution.minMeetingRooms(intervals)) # Output: 1

intervals = [[1, 2], [2, 4], [7, 8], [4, 5]]
print(solution.minMeetingRooms(intervals)) # Output: 1