'''
581. Shortest Unsorted Continuous Subarray

Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0 

Constraints:
1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

Follow up: Can you solve it in O(n) time complexity?
'''
from typing import List

# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         max = nums[len(nums)-1]
#         min = nums[0]
#         start, end = -1, -1
#         left_index = 0
#         right_index = len(nums)-1

#         while left_index<len(nums)-1:
#             if nums[left_index+1] > nums[left_index]:
#                 max = nums[left_index+1]
#             else:
#                 max = nums[left_index]
#                 end = left_index
#             left_index += 1
        
#         while right_index>0:
#             if nums[right_index-1] < nums[right_index]:
#                 min = nums[right_index-1]
#             else:
#                 min = nums[right_index]
#                 start = right_index
#             right_index -= 1
        
#         while start>0:
#             if nums[start-1] > min:
#                 start-=1
#             else:
#                 break
        
#         while end<len(nums)-1:
#             if nums[end+1] < max:
#                 end+=1
#             else:
#                 break
        
#         if start == -1:
#             return 0
            
#         return end-start+1

            
'''
Attemtp 7+
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_length = len(nums)
        left, right = 0, nums_length-1
        max_index, min_index = 0, nums_length-1
        end, start = None, None

        while left < nums_length-1:
            if nums[left] > nums[left+1]:
                end = left
                if nums[left] > nums[max_index]:
                    max_index = left
            left+=1
        
        while right > 0:
            if nums[right] < nums[right-1]:
                start = right
                if nums[right] < nums[min_index]:
                    min_index = right
            right-=1
        
        if start is None or end is None:
            return 0
        
        while end<nums_length-1:
            if nums[end+1]<nums[max_index]:
                end+=1
            else:
                break

        while start>0:
            if nums[start-1]>nums[min_index]:
                start-=1
            else:
                break
            
        # print(nums, nums[start:end+1], nums[min_index], nums[max_index])
        return end-start+1


'''
AI code but so much clear and better
'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = -1, -1
        max_seen, min_seen = float('-inf'), float('inf')

        # Left to right: identify right boundary
        for i in range(n):
            if nums[i] < max_seen:
                end = i
            else:
                max_seen = nums[i]

        # Right to left: identify left boundary
        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                start = i
            else:
                min_seen = nums[i]

        if start == -1:  # Already sorted
            return 0

        return end - start + 1

        
solution = Solution()

nums = [2,6,4,8,10,9,15]
print(solution.findUnsortedSubarray(nums))

nums = [1,2,3,4]
print(solution.findUnsortedSubarray(nums))

nums = [1]
print(solution.findUnsortedSubarray(nums))

nums = [2,1]
print(solution.findUnsortedSubarray(nums))

nums = [1,2]
print(solution.findUnsortedSubarray(nums))

nums = [1,3,2,4,5]
print(solution.findUnsortedSubarray(nums))

nums = [1,3,5,4,2]
print(solution.findUnsortedSubarray(nums))

nums = [1,2,3,5,4]
print(solution.findUnsortedSubarray(nums))