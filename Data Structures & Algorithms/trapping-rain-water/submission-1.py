class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        maxLeft= height[left]
        maxRight = height[right]
        area = 0
        while left<right:
            if maxLeft < maxRight:
                left+=1
                h = maxLeft- height[left] 
                area += max(0,h)
                if height[left] > maxLeft:
                    maxLeft = height[left]
            else:
                right-=1
                h = maxRight- height[right]
                area+= max(0,h)
                if height[right] > maxRight:
                    maxRight = height[right]

        return area