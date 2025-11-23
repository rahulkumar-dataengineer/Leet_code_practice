'''
Maximum CPU Load from the given list of jobs
https://www.geeksforgeeks.org/dsa/maximum-cpu-load-from-the-given-list-of-jobs/

Given an array of jobs with different time requirements, where each job consists of start time, end time and CPU load. 
The task is to find the maximum CPU load at any time if all jobs are running on the same machine.


Examples: 

Input: jobs[] = [[1, 4, 3], [2, 5, 4], [7, 9, 6]] 
Output: 7 
Explanation: 
In the above-given jobs, there are two jobs which overlaps. 
That is, Job [1, 4, 3] and [2, 5, 4] overlaps for the time period in [2, 4] 
Hence, the maximum CPU Load at this instant will be maximum (3 + 4 = 7).


Input: jobs[] = [[6, 7, 10], [2, 4, 11], [8, 12, 15]] 
Output: 15 
Explanation: 
Since, There are no jobs that overlaps. 
Maximum CPU Load will be - max(10, 11, 15) = 15  
'''

from typing import List

class Solution:
    def maxCpuLoad(self, jobs: List[List[int]]) -> int:
        jobs.sort(key=lambda x: x[0])
        result = []
        start = 0
        end = 1
        load = 2
        length = len(jobs)
        max_load = 0

        for job in range(1, length):
            inter_start = max(jobs[job - 1][start],jobs[job][start])
            inter_end = min(jobs[job - 1][end],jobs[job][end])

            if inter_start <= inter_end:
                load_time = jobs[job - 1][load] + jobs[job][load]
                max_load = max(max_load, load_time)
                result.append([inter_start, inter_end, max_load])
        
        print(result) 

        if max_load == 0:
            return max(x[load] for x in jobs)
       
        return max_load




solution = Solution()
jobs = [[1, 4, 3], [2, 5, 4], [7, 9, 6]] 
print(solution.maxCpuLoad(jobs)) # 7

jobs = [[6, 7, 10], [2, 4, 11], [8, 12, 15]] 
print(solution.maxCpuLoad(jobs)) # 15