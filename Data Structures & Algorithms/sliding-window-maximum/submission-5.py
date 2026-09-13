class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(k):
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            dq.append([nums[i],i])

        res.append(dq[0][0])
        for i in range(k,len(nums)):
            while dq and dq[-1][0] < nums[i]:
                dq.pop()
            while dq and dq[0][1] <= i - k:
                dq.popleft()
            dq.append([nums[i],i])
            res.append(dq[0][0])
        return res