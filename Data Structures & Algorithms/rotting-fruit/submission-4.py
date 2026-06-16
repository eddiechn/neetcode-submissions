class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        time = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        fresh = 0


        q = deque()
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(nrows) and nc in range(ncols) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1 
             
            
            





        