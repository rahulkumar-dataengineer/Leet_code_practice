'''
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
'''
from typing import Optional
from helper.LinkedLists import ListNode, LinkedList

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = head

        while n>0 and right:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
    

solution = Solution()
ll = LinkedList()


head = [1,2,3,4,5]
n = 2
head = ll.listToLinkedList(head)
ll.printList(head)
ll.printList(solution.removeNthFromEnd(head,n)) # Output: [1,2,3,5]


head = [1]
n = 1
head = ll.listToLinkedList(head)
ll.printList(head)
ll.printList(solution.removeNthFromEnd(head,n)) # Output: []


head = [1,2]
n = 1
head = ll.listToLinkedList(head)
ll.printList(head)
ll.printList(solution.removeNthFromEnd(head,n)) # Output: [1]