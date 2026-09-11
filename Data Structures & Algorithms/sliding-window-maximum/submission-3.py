class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(len(nums)):
            # 1. Remove elements from the front that are out of the window's bounds
            # i - k is the index just before the start of our current window
            if dq and dq[0][1] <= i - k:
                dq.popleft()
            
            # 2. Maintain monotonic decreasing order (pop smaller elements from the back)
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            
            # 3. Add the current element to the back
            dq.append([nums[i], i])
            
            # 4. Once we have processed at least 'k' elements, start adding to result
            if i >= k - 1:
                res.append(dq[0][0]) # The front of the deque is always the max
                
        return res

            