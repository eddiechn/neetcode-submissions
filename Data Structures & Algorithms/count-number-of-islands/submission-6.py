class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        go through the grid, when we encounter an island, we run dfs on that tile
        increment res += 1
        """
        res = 0
        nrows = len(grid)
        ncols = len(grid[0])


        def dfs(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or grid[r][c] != "1":
                return 


            if grid[r][c] == "1":
                grid[r][c] = "*"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c+ 1)
            dfs(r, c -1)


        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1


        return res
        