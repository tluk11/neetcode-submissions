# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a,b = list1,list2
        head = None
        if not a:
            return list2
        elif not b: 
            return list1
        if a and b:
            if a.val < b.val:
                head = a
                a = a.next
            else:
                head = b
                b = b.next
        node = head
        while a and b:
            if a.val < b.val:
                node.next = a
                a = a.next
            else:
                node.next = b
                b = b.next
            node = node.next
        if a:
            node.next = a
        elif b:
            node.next = b
        return head
