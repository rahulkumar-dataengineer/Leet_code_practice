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
   
    # duplicate n times and shift right
    def duplicateZerosNspacesShiftRight(self, arr: list[int], n: int) -> None:
        zero_count = 0
        for element in arr:
            if element == 0:
                zero_count+=n
        
        left_index = len(arr)-1
        right_index = left_index + zero_count

        while left_index!=right_index:
            if right_index<=len(arr)-1:
                arr[right_index] = arr[left_index]
            right_index-=1

            if arr[left_index] == 0:
                for i in range(n):
                    if right_index<=len(arr)-1:
                        arr[right_index] = arr[left_index]
                    right_index-=1     
            left_index-=1
    
    # duplicate n times and shift left
    def duplicateZerosNspacesShiftLeft(self, arr: list[int], n: int) -> None:
        zero_count = 0
        for value in arr:
            if value == 0:
                zero_count+=n
        
        right_index = 0
        left_index = 0 - zero_count

        length = len(arr)
        while left_index < length:
            if left_index >= 0:
                arr[left_index] = arr[right_index]
            left_index+=1

            if arr[right_index] == 0:
                for i in range(n):
                    if left_index >= 0:
                        arr[left_index] = arr[right_index]
                    left_index+=1
            right_index+=1



# Example usage:
solution = Solution()

arr = [1,0,2,3,0,4,5,0]
print(arr, "\n-----------------------------------")

# solution.duplicateZerosOnceShiftRight(arr)
# print(arr)

arr = [1,0,2,3,0,4,5,0]
n = 1
solution.duplicateZerosNspacesShiftRight(arr, n)
print(arr)

arr = [1,0,2,3,0,4,5,0]
n = 2
solution.duplicateZerosNspacesShiftRight(arr, n)
print(arr)

arr = [1,0,2,3,0,4,5,0]
n = 3
solution.duplicateZerosNspacesShiftRight(arr, n)
print(arr)

print("\n-----------------------------------")

arr = [1,0,2,3,0,4,5,0]
n = 1
solution.duplicateZerosNspacesShiftLeft(arr, n)
print(arr)

arr = [1,0,2,3,0,4,5,0]
n = 2
solution.duplicateZerosNspacesShiftLeft(arr, n)
print(arr)  

arr = [1,0,2,3,0,4,5,0]
n = 3
solution.duplicateZerosNspacesShiftLeft(arr, n)
print(arr)

            








        