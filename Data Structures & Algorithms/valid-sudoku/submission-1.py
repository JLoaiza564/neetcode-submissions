class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            seen = set()
            for n in r:
                if n.isdigit():
                    if n in seen:
                        return False
                    seen.add(n)

        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c].isdigit() and board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for r in range(0, 6, 3):
            for c in range(0, 6, 3):
                seen = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if board[i][j].isdigit() and board[i][j] in seen:
                            return False
                        seen.add(board[i][j])


        return True
