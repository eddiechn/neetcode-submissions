class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or grid[r][c] != "1":
                return 

            grid[r][c] = "*"
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)


        res = 0 
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)



        return res
