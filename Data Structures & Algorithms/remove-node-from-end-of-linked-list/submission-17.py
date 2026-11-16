# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)       # el falso apunta a la cabeza
        prev = dummy

        for i in range(length - n):         # ¿cuántos pasos?
            prev = prev.next
        prev.next = prev.next.next            # saltarse el nodo
        return dummy.next