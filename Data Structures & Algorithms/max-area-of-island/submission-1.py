class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows,cols = len(grid),len(grid[0])
        def dfs(y,x):
            if x >= cols or y >= rows or x < 0 or y < 0 or grid[y][x]!= 1:
                return 0
            grid[y][x] = 0 
            return 1 + dfs(y,x+1) + dfs(y,x-1) + dfs(y-1,x) + dfs(y+1,x)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count = dfs(i,j)
                    res = max(res,count)

        return res


            