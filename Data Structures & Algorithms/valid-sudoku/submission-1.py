class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = defaultdict(list)
        n = len(board)
        # row check 
        for r in range(n):
            row = set()
            for c in range(n):        
                if board[r][c] in row:
                    return False
                if board[r][c] != ".":
                    row.add(board[r][c])
                    grid[board[r][c]].append((r,c))

        # col check
        for c in range(n):
            col = set()
            for r in range(n):
                if board[r][c] in col:
                    return False
                if board[r][c] != ".":
                    col.add(board[r][c])


        # 3x3 check 
        for key in grid.keys():
            loc = set()
            for r,c in grid[key]:
                row, col = 0,0 
                if r >= 3 and r <= 5:
                    row = 1
                elif r > 5:
                    row = 2
                if c >= 3 and c <= 5:
                    col = 1
                elif c > 5:
                    col = 2
                if (row,col) in loc:
                    return False
                loc.add((row,col))
        return True
                    
                    
