'''
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
'''

from typing import Optional
from helper.LinkedLists import ListNode, LinkedList

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = head

        length = head
        count = 1
        while length.next:
            length = length.next
            count+=1
        
        k = k % count
        if k == 0:
            return head
        
        while k>0 and right:
            right = right.next
            k-=1
        
        while right:
            left = left.next
            right = right.next
        
        new_head = left.next
        left.next = None
        length.next = dummy.next

        return new_head
        




solution = Solution()
ll = LinkedList()

head = [1,2,3,4,5]
k = 2
# Output: [4,5,1,2,3]
head = ll.listToLinkedList(head)
ll.printList(head)
ll.printList(solution.rotateRight(head,k))


head = [0,1,2]
k = 4
# Output: [2,0,1]
head = ll.listToLinkedList(head)
ll.printList(head)
ll.printList(solution.rotateRight(head,k))



