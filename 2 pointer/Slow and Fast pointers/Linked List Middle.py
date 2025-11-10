'''
876.. Middle of Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
from typing import Optional
from helper.LinkedLists import ListNode, LinkedList

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow



solution = Solution()
ll = LinkedList()


head = [1,2,3,4,5]
head = ll.listToLinkedList(head)
ll.printList(head)
print(solution.middleNode(head)) # Output: True


head = [1,2,3,4,5,6]
head = ll.listToLinkedList(head)
ll.printList(head)

print(solution.middleNode(head)) # Output: True


# head = [1]
# pos = -1
# head = ll.listToLinkedList(head)
# ll.printList(head)
# ll.connect_tail_to_pos(head, pos)
# print(solution.hasCycle(head)) # Output: False