class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        time = 0
        q = deque()
        fresh = 0

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        if fresh == 0: return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr in range(nrows) and nc in range(ncols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr, nc])
                        fresh -= 1

            time += 1


        return time if fresh == 0 else -1
                


