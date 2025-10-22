'''
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

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
        dummy = ListNode()
        dummy.next = head
        prev_node = dummy
        current_node = head

        while current_node and current_node.next is not None:
            if current_node.val == current_node.next.val:
                while current_node.next is not None and current_node.val == current_node.next.val:
                    current_node = current_node.next
                prev_node.next = current_node.next
            else:
                prev_node = current_node
            current_node = current_node.next    
        return dummy.next

            
                
# Example usage:
solution = Solution()
ll = LinkedList()

# arr = [1,2,3,3,4,4,5,6,7]
arr = [1,1,1,2,3]

head = ll.listToLinkedList(arr)
ll.printList(head)

new_head = solution.deleteDuplicates(head)
ll.printList(new_head)