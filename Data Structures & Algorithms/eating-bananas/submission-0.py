class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left,right= 1,max(piles)
        mid = 0
        while left<=right:
            mid = (left+right)//2
            count = 0
            for pile in piles:
                count+= math.ceil(pile/mid)
            if count <= h:
                right = mid-1
            else:
                left = mid+1

        return left

        