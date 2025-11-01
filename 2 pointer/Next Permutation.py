'''
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left = length-2
        right = length-1

        # find pivot index from right side
        while left>=0 and nums[left]>=nums[left+1]:
            left-=1
        
        if left<0:
            return nums.sort()
        
        # find max index which needs to be swapped with pivot
        while right>left and nums[right]<=nums[left]:
            right-=1
        
        # swap the values
        nums[left], nums[right] = nums[right], nums[left]

        # sort the array from left+1 - after the pivot
        nums[left+1:] = sorted(nums[left+1:])

        



            
                

solution = Solution()

nums = [1,2,3]
print(nums)
solution.nextPermutation(nums)
print(nums, "\n----------------------------------") #[1,3,2]


nums = [3,2,1]
print(nums)
solution.nextPermutation(nums)
print(nums, "\n----------------------------------") #[1,2,3]

nums = [1,1,5]
print(nums)
solution.nextPermutation(nums)
print(nums, "\n----------------------------------") #[1,5,1]

nums = [1,2,3,5,4,2]
print(nums)
solution.nextPermutation(nums)
print(nums, "\n----------------------------------") #[1,2,4,2,3,5]

nums = [2,3,1]
print(nums)
solution.nextPermutation(nums)
print(nums, "\n----------------------------------") #[3,1,2]

nums = [1,3,2]
print(nums)
solution.nextPermutation(nums)
print(nums, "\n----------------------------------") #[2,1,3]

nums = [1,5,1]
print(nums)
solution.nextPermutation(nums)
print(nums, "\n----------------------------------") #[5,1,1]


