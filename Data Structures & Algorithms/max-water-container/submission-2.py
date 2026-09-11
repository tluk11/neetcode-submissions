class Solution:
    def maxArea(self, heights: List[int]) -> int:
        beg,end = 0,len(heights)-1
        area = 0

        while beg<end:
            height = min(heights[beg],heights[end])
            width = end-beg
            area = max(area,height*width)
            if heights[beg]>heights[end]:
                end-=1
            elif heights[beg]<heights[end]:
                beg+=1
            else:
                beg+=1
        return area