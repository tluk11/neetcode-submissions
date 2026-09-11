class Solution:
    def maxArea(self, heights: List[int]) -> int:
        beg,end = 0,len(heights)-1
        area = 0

        while beg<end:
            minheight = min(heights[beg],heights[end])
            area = max(area,minheight*(end-beg))
            if heights[beg]<heights[end]:
                beg+=1
            else:
                end-=1
        return area 