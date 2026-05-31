# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one pass
        

        dummy = ListNode(-1)

        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        # remove
        node = slow.next
        slow.next = node.next
        node.next = None

        return dummy.next
            
