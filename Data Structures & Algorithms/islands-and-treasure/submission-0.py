class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row,col = len(grid),len(grid[0])
        def dfs(r,c,dist):
            if r >= row or r < 0 or c >= col or c < 0 or grid[r][c] < dist:
                return
            grid[r][c] = dist
            dfs(r+1,c,dist+1)
            dfs(r-1,c,dist+1)
            dfs(r,c+1,dist+1)
            dfs(r,c-1,dist+1)

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    dfs(x+1,y,1)
                    dfs(x-1,y,1)
                    dfs(x,y+1,1)
                    dfs(x,y-1,1)