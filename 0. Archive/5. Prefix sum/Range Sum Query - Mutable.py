'''
307. Range Sum Query - Mutable

!!!! later

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:
1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 10^4 calls will be made to update and sumRange.
'''

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(self.nums)
        self._prefixSum()
    
    def _prefixSum(self):
        self.prefix = [0] * self.length
        self.prefix[0] = self.nums[0]

        for index in range(1, self.length):
            self.prefix[index] = self.prefix[index - 1] + self.nums[index]
    
    
    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self._prefixSum()
           

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        
        return self.prefix[right] - self.prefix[left - 1]
        


nums = [1, 3, 5]

queries = [
    [0, 2], 
    [1, 2], 
    [0, 2]
]

obj = NumArray(nums)

print(obj.sumRange(queries[0][0], queries[0][1]))
print(obj.update(queries[1][0], queries[1][1]))
print(obj.sumRange(queries[2][0], queries[2][1]))