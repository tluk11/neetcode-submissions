# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: find middle (slow = beg, fast = end)
        beg = head
        end = head
        while end and end.next:
            beg = beg.next
            end = end.next.next
        
        # Step 2: reverse second half
        prev = None
        curr = beg.next
        beg.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3: merge two halves
        f, s = head, prev   # <-- use prev (reversed head), not curr
        while s:
            tmp1, tmp2 = f.next, s.next
            f.next = s
            s.next = tmp1
            f, s = tmp1, tmp2
