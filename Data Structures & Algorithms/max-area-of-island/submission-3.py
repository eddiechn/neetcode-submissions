class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        nrows, ncols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= nrows or j >= ncols or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            
            return (1+ 
            dfs(i + 1, j) +  
            dfs(i -1 , j) + 
            dfs(i, j + 1) + 
            dfs(i, j -1)
            )

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    local = dfs(r, c)
                    res = max(local, res)


        return res




        