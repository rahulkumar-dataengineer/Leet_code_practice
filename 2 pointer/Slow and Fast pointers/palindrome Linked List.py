'''
234.Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 
Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''
from typing import Optional
from helper.LinkedLists import ListNode, LinkedList

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True




solution = Solution()
ll = LinkedList()


head = [1,2,3,2,1]
head = ll.listToLinkedList(head)
ll.printList(head)
print(solution.isPalindrome(head)) # Output: True


head = [1,2]
head = ll.listToLinkedList(head)
ll.printList(head)
print(solution.isPalindrome(head)) # Output: True


# head = [1]
# pos = -1
# head = ll.listToLinkedList(head)
# ll.printList(head)
# ll.connect_tail_to_pos(head, pos)
# print(solution.hasCycle(head)) # Output: False