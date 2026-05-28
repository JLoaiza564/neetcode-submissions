from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                digit = board[r][c]
                if not digit.isdigit():
                    continue

                squares_map_key = ((r//3)*3 + c//3)
                if digit in rows[r] or digit in columns[c] or digit in squares[squares_map_key]:
                    return False

                rows[r].add(digit)
                columns[c].add(digit)
                squares[squares_map_key].add(digit)

        return True