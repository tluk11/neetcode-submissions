class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right # Store the best speed here
        
        while left <= right:
            mid = (left + right) // 2
            
            # Efficiently calculate total time using a generator expression
            time = sum(math.ceil(pile / mid) for pile in piles)
            
            if time <= h:
                res = mid       # This speed works, record it
                right = mid - 1 # Try an even slower speed
            else:
                left = mid + 1  # Too slow, must eat faster
                
        return res 
            