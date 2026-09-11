# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        f,s = dummy,head
        
        while n > 0:
            s = s.next
            n-=1
        while s:
            s = s.next
            f = f.next
        f.next = f.next.next

        return dummy.next