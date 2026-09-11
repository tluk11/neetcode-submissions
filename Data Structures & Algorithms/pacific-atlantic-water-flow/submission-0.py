class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights),len(heights[0])
        # for pacific top side
        pacific = set()
        for c in range(COLS):
            pacific.add((0,c)) 
        # pacific left side
        for r in range(ROWS):
            pacific.add((r,0))
        atlantic = set()
        # for atlantic bottom side
        for c in range(COLS):
            atlantic.add((ROWS-1,c))
        # atlantic right side 
        for r in range(ROWS):
            atlantic.add((r,COLS-1))
        
        def dfs(r,c,visited,value):
            if r < 0 or r >= ROWS or c < 0  or c >= COLS or (r,c) in visited:
                return 
            if heights[r][c] >= value:
                val = heights[r][c]
                visited.add((r,c))
                dfs(r+1,c,visited,val)
                dfs(r-1,c,visited,val)
                dfs(r,c+1,visited,val)
                dfs(r,c-1,visited,val)
            return
        pvisit = set()
        for r,c in pacific:
            dfs(r,c,pvisit,0)
        avisit = set()
        for r,c in atlantic:
            dfs(r,c,avisit,0)
        res = []
        for r,c in pvisit:
            if (r,c) in avisit:
                res.append([r,c])

        return res


