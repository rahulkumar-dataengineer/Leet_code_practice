'''
1314. Matrix Block Sum

Given a m x n matrix mat and an integer k, return a matrix answer where each answer[row][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
 

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
'''

from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ROW = len(mat)
        COL = len(mat[0])

        prefix_sum = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for row in range(1, ROW+1):
            for col in range(1, COL+1):
                curr_val = mat[row - 1][col - 1]
                left_rc = prefix_sum[row][col - 1]
                top_rc = prefix_sum[row - 1][col]
                overlap = prefix_sum[row - 1][col - 1]

                prefix_sum[row][col] = curr_val + left_rc + top_rc - overlap

        output = [[0] * COL for _ in range(ROW)]

        for row in range(1, ROW+1):
            for col in range(1, COL+1):
                
                r_idx = row - 1
                c_idx = col - 1

                row1 = max(0, r_idx - k) + 1
                col1 = max(0, c_idx - k) + 1
                row2 = min(ROW - 1, r_idx + k) + 1
                col2 = min(COL - 1, c_idx + k) + 1

                big_rc = prefix_sum[row2][col2]
                top_rc = prefix_sum[row1 - 1][col2]
                left_rc = prefix_sum[row2][col1 - 1]
                overlap = prefix_sum[row1 - 1][col1 - 1]
                
                output[row - 1][col - 1] = big_rc - top_rc - left_rc + overlap

        return output


solution = Solution()

matrix = [
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
]

k = [1, 2]

for index in range(len(matrix)):
    print(solution.matrixBlockSum(matrix[index], k[index]))