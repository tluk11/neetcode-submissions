# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        beg,end = head,head

        while end and end.next:
            end = end.next.next
            beg = beg.next

        prev = None
        curr = beg.next
        beg.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        f,s = head,prev
        while s:
            t1,t2 = f.next,s.next
            f.next = s
            s.next = t1
            f,s = t1,t2