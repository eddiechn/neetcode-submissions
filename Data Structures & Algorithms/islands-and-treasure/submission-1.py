class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        -1 represents a water cell that cannot be traversed
        0 : a treasure chest
        INF -> cell that can be traversed
        
        bfs from out treasures. 
        """

        nrows, ncols = len(grid), len(grid[0])
        visit = set()
        q = deque()


        def addCell(r, c):
            if r < 0 or c < 0 or r >= nrows or c >= ncols or (r, c) in visit or grid[r][c] == -1:
                return 

            visit.add((r, c))
            q.append([r, c])


        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))


        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            dist += 1



        


        