class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fresh = 0
        q = deque()
        time = 0
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 2:
                    q.append((r, c))

                elif grid[r][c] == 1:
                    fresh += 1


        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nr < nrows and nc < ncols and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))


            time += 1


        return time if fresh == 0 else -1
        

        