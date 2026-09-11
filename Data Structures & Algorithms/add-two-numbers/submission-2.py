# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = 1 
        n1 = l1
        num1 = 0
        while n1:
            temp = p1*n1.val
            num1+=temp
            p1*=10
            n1 = n1.next
        p2 = 1 
        n2 = l2
        num2 = 0
        while n2:
            temp = p2*n2.val
            num2+=temp
            p2*=10
            n2 = n2.next
        num3 = num1+num2
        if num3 == 0:
            return ListNode(0)
        dummy = ListNode()
        curr = dummy
        while num3>0:
            curr.next = ListNode(num3%10)
            num3 = num3//10
            curr = curr.next
        
        return dummy.next