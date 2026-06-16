class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nrows, ncols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == nrows or c == ncols or board[r][c] != "O":
                return

            board[r][c] = "A"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(nrows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][ncols - 1] == "O":
                dfs(r, ncols - 1)

        for c in range(ncols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[nrows - 1][c] == "O":
                dfs(nrows - 1, c)


        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "A":
                    board[r][c] = "O"
