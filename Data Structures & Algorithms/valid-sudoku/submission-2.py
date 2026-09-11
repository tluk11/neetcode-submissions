class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in rows[r] or board[r][c] in cols[c]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    x,y = 1,1
                    if r <= 2:
                        x = 0
                    elif r >= 6:
                        x = 2

                    if c <= 2:
                        y = 0
                    elif c >= 6:
                        y = 2

                    if board[r][c] in grid[(x,y)]:
                        return False
                    grid[(x,y)].add(board[r][c])

        return True 
