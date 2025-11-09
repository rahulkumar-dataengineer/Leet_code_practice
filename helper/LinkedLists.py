from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


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

    def connect_tail_to_pos(self, head: Optional[ListNode], pos: int) -> Optional[ListNode]:
        if head is None or pos < 0:
            return head
        # find target node at index pos
        target = head
        for _ in range(pos):
            if target is None:
                return head  # pos out of range
            target = target.next
        if target is None:
            return head

        # find tail
        tail = head
        while tail.next:
            tail = tail.next

        # connect tail to target to create a cycle
        tail.next = target
        return head
