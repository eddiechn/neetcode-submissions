class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        run dfs from the outside cells.
        convert them to a temp, 
        """

        nrows = len(board)
        ncols = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or board[r][c] != "O":
                return 

            if board[r][c] == "O":
                board[r][c] = "*"

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c) 


        for r in range(nrows):
            dfs(r, 0)
            dfs(r, ncols - 1)

        for c in range(ncols):
            dfs(0, c)
            dfs(nrows - 1, c)


        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "*":
                    board[r][c] = "O"       