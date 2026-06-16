class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        keep track of max island area
        go through grid, when we find a isnaldn tile, perform dfs on it

        """
        res = 0
        nrows = len(grid)
        ncols = len(grid[0])


        def dfs(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or grid[r][c] != 1:
                return 0

            if grid[r][c] == 1:
                grid[r][c] = 0
                return (1 + 
                dfs(r + 1, c) + 
                dfs(r - 1, c) + 
                dfs(r, c + 1) + 
                dfs(r, c - 1))

            return 0


        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))


        return res      