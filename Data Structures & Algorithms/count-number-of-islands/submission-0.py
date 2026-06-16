class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if i < 0 or i >= nrows or j < 0 or j >= ncols or grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)




        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands

        