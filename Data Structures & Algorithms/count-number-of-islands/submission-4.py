class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        
        def dfs(x,y):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] != "1":
                return 
            grid[x][y] = "0"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1": 
                    count += 1
                    dfs(i,j)
                
        return count
