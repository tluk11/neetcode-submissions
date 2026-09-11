class Solution:
    def trap(self, height: List[int]) -> int:
        leftwall,rightwall = height[0],height[len(height)-1]
        left,right = 0,len(height)-1
        minwall = min(leftwall,rightwall)
        floor = minwall
        res = 0
        while left<right:
            if height[left] < height[right]:
                left+=1
                floor = height[left]
                if height[left] > leftwall:
                    leftwall = height[left]
            else:
                right-=1
                floor = height[right]
                if height[right] > rightwall:
                    rightwall = height[right]
            minwall = min(rightwall,leftwall)
            if floor < minwall:
                res+= minwall-floor

        return res

            

            
        