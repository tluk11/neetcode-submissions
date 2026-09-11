class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        
        group_prev = dummy  # track node before the group

        while True:
            # find the kth node from group_prev
            end = group_prev
            for i in range(k):
                end = end.next
                if not end:   # not enough nodes left
                    return dummy.next

            beg = group_prev.next
            next_group = end.next

            # reverse the group
            prev, curr = next_group, beg
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # reconnect
            group_prev.next = end
            group_prev = beg
