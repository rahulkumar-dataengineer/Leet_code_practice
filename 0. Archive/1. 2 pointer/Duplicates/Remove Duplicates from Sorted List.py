'''
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class LinkedList:
    def printList(self, head: Optional[ListNode]) -> None:
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
    def listToLinkedList(self, arr: list[int]) -> Optional[ListNode]:
        if not arr:
            return None
        
        head = ListNode(arr[0])
        current = head

        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next 
        
        return head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solution 1
        if head is not None:
            current_node = head
            next_node = current_node.next
        else:
            return head

        while next_node is not None:
            if current_node.val == next_node.val:
                next_node = next_node.next
            else:
                current_node.next = next_node
                current_node = next_node
                next_node = next_node.next
        current_node.next = None
        return head

        # # solution 2
        
        # res = head

        # while head.next is not None:
        #     if head.val == head.next.val:
        #         head.next = head.next.next
        #     else:
        #         head = head.next
        
        # return res

          
                
# Example usage:
solution = Solution()
ll = LinkedList()

# arr = [1,1,2]
# arr = []
arr = [1,1,2,3,3,3]

head = ll.listToLinkedList(arr)
ll.printList(head)

new_head = solution.deleteDuplicates(head)
ll.printList(new_head)