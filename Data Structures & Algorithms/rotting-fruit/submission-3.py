class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # keep track of total oranges
        # keep track of num of rotten oranges at the end to see if they match the original
        # Use BFS + queue
        q = deque()
        ROWS,COLS = len(grid),len(grid[0])
        fresh = 0
        minutes = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c,0))
                    grid[r][c] = 1
                    fresh+=1
        while q:
            r,c,time = q.popleft()
            if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 1:
                fresh-=1
                grid[r][c] = 2
                q.append((r+1,c,time+1))
                q.append((r-1,c,time+1))
                q.append((r,c+1,time+1))
                q.append((r,c-1,time+1))
                minutes = time
        if fresh > 0:
            return -1
        return minutes 
