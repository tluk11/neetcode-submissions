class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def subBoxValid():
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            val = board[box_row + i][box_col + j]
                            if val != '.':
                                if val in seen:
                                    return False
                                seen.add(val)
            return True
        def rowValid():
            for y in range(9):
                mySet = set()
                for x in range(9):
                    if board[x][y] != '.':
                        if board[x][y] in mySet:
                            return False
                        else:
                            mySet.add(board[x][y])
            return True
        def colValid():
            for x in range(9):
                mySet = set()
                for y in range(9):
                    if board[x][y] != '.':
                        if board[x][y] in mySet:
                            return False
                        else:
                            mySet.add(board[x][y])
            return True

        return subBoxValid() and rowValid() and colValid()
                        