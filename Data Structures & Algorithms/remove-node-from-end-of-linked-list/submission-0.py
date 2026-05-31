# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for _ in range(length - n):
            prev = prev.next

        # remove
        node = prev.next
        prev.next = node.next
        node.next = None

        return dummy.next