# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find middle 

        def find_middle(head):
            fast = head
            slow = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow
        
        def reverse(head):
            cur = head
            prev = None

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        middle = find_middle(head)
        reverse_head = reverse(middle.next)
        middle.next = None
        dummy = ListNode()
        left = head
        right = reverse_head
        cur = dummy
        while right:
            left_next = left.next
            right_next = right.next
            cur.next = left
            cur.next.next = right
            cur = cur.next.next
            right = right_next
            left = left_next
        if left:
            cur.next = left



