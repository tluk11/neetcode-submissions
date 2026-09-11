# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev,remove,end = None, head, head
        i = 0
        while end and i < n:
            end = end.next
            i+=1


        while end:
            prev = remove
            remove=remove.next
            end=end.next
        if prev == None:
            return remove.next
        prev.next = remove.next

        return head