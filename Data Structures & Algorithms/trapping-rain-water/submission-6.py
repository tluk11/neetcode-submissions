class Solution:
    def trap(self, height: List[int]) -> int:
        beg,end = 0,len(height)-1
        leftwall, rightwall = height[beg],height[end]
        res = 0
        while beg<end:
            floor = 0
            if height[beg] < height[end]:
                beg+=1
                floor = height[beg]
                if height[beg] > leftwall:
                    leftwall = height[beg]
            else:
                end-=1
                floor = height[end]
                if height[end] > rightwall:
                    rightwall = height[end]
            
            if leftwall > floor and rightwall>floor:
                res+= min(leftwall,rightwall)-floor
            
        return res
            
