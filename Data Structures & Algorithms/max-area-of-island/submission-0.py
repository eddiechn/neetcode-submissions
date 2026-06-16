class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        nrows, ncols = len(grid), len(grid[0])


        def dfs(r, c):
           

            if r < 0 or c < 0 or r >= nrows or c >= ncols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return (1 + dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))

           
        
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    local = dfs(r, c)
                    maxArea = max(maxArea, local)


        return maxArea
        