class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        nrows = len(heights)
        ncols = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= nrows or c >= ncols or heights[r][c] < prevHeight \
            or (r, c) in visit:
                return 

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1,  visit, heights[r][c])


        for c in range(ncols):
            dfs(0, c, pac, heights[0][c])
            dfs(nrows - 1, c, atl, heights[nrows - 1][c])

        for r in range(nrows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, ncols - 1, atl, heights[r][ncols - 1])

        for r in range(nrows):
            for c in range(ncols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))


        return res



        