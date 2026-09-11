# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = None
        if not curr1:
            return list2
        if not curr2:
            return list1
        if curr1.val < curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next
        main = head
        while curr1 and curr2:
            if curr1.val < curr2.val:
                main.next = curr1
                curr1 = curr1.next
            else:
                main.next = curr2
                curr2 = curr2.next
            main = main.next
        if not curr1 and curr2:
            main.next = curr2
        if not curr2 and curr1:
            main.next = curr1
        return head

            