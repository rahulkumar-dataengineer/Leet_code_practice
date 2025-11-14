'''
Max Sum Subarray of size K
https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:
Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.

Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.

Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.

Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^6
1 ≤ k ≤ arr.size()
'''

class Solution:
    def maxSubarraySum(self, arr, k):
        length = len(arr)
        total = maximum = sum(arr[0:k])
        left = 0
        right = k

        while right < length:
            total += arr[right]-arr[left]
            if total > maximum:
                maximum = total
            left+=1
            right+=1
        return maximum

solution = Solution()

arr = [100, 200, 300, 400]
k = 2
print(solution.maxSubarraySum(arr, k)) #Output: 700

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(solution.maxSubarraySum(arr, k)) #Output: 39

arr = [100, 200, 300, 400]
k = 1
print(solution.maxSubarraySum(arr, k)) #Output: 400