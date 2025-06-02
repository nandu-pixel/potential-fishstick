def solveNQueens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def place_queen(row):
        if row == n:
            board = ["".join(r) for r in grid]
            solutions.append(board)
            return
        for col in range(n):
            if is_safe(row, col):
                grid[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                place_queen(row + 1)

                grid[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

    solutions = []
    cols, diag1, diag2 = set(), set(), set()
    grid = [['.' for _ in range(n)] for _ in range(n)]
    place_queen(0)
    return solutions
