'''
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
'''
from typing import Optional
from helper.LinkedLists import ListNode, LinkedList

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        - Find middle
        - reverse from middle
        - merge the 2 LL
        '''
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        half_2 = slow.next
        slow.next = None
        
        prev = None
        while half_2:
            temp = half_2.next
            half_2.next = prev
            prev = half_2
            half_2 = temp
        
        left = head
        right = prev

        while right:
            temp = left.next
            left.next = right

            temp2 = right.next
            right.next = temp

            left = temp
            right = temp2


solution = Solution()
ll = LinkedList()

head = [1,2,3,4]
head = ll.listToLinkedList(head)
ll.printList(head)
solution.reorderList(head)
ll.printList(head) # Output: [1,4,2,3]


head = [1,2,3,4,5]
head = ll.listToLinkedList(head)
ll.printList(head)
solution.reorderList(head)
ll.printList(head) # Output: [1,5,2,4,3]


