class Solution:
    # duplicate once and shift right
    def duplicateZerosOnceShiftRight(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_count = 0
        for value in arr:
            if value == 0:
                zero_count+=1
        
        left_index = len(arr)-1
        right_index = left_index + zero_count

        while left_index != right_index:
            if right_index <= len(arr) - 1:
                arr[right_index] = arr[left_index]
            right_index-=1

            if arr[left_index] == 0:
                if right_index <= len(arr) - 1:
                    arr[right_index] = arr[left_index]
                right_index-=1
            left_index-=1   
    
    def duplicateZerosNspacesShiftRight(self, arr: list[int]) -> None:
        



# Example usage:
solution = Solution()

arr = [1,0,2,3,0,4,5,0]
print(solution.duplicateZerosOnceShiftRight(arr))

arr = [1,0,2,3,0,4,5,0]
print(solution.duplicateZerosOnceShiftRight(arr))



            








        