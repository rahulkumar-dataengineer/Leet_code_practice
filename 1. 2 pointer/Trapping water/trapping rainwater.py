'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
'''


'''
at every index, what is the max left, right. maximum water we can store is min of the 2 boundries - height of index.
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_index = 1
        right_index = len(height)-2
        max_left = height[0]
        max_right = height[len(height)-1]
        count = 0

        while left_index<=right_index:
            if max_left <= max_right:
                total = max_left - height[left_index]
                max_left = max(height[left_index], max_left)
                left_index+=1
            else:
                total = max_right - height[right_index]
                max_right = max(height[right_index], max_right)
                right_index-=1

            if total > 0:
                count += total

        return count



solution = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1] #6
print(height, "\t", solution.trap(height))

height = [4,2,0,3,2,5] #9
print(height, "\t" ,solution.trap(height))