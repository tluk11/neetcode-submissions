import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy   # pointer to build result
        heap = []

        # put the first node of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # keep popping smallest element until heap is empty
        while heap:
            val, i, node = heapq.heappop(heap)
            res.next = node
            res = res.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
