# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first, second = head, prev
        
        # We only need to check 'second' because the second half is always
        # equal to or 1 node shorter than the first half.
        while second:
            # Save the next nodes
            tmp1, tmp2 = first.next, second.next
            
            # Link first -> second
            first.next = second
            # Link second -> first's next
            second.next = tmp1
            
            # Advance both pointers
            first, second = tmp1, tmp2
