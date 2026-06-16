class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, src, 0)]
    
        best = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost

            if node in best and best[node] < stops:
                continue
            best[node] = stops

        
            if stops <= k:
                for u, v in graph[node]:
                    heapq.heappush(heap, (cost + v, u, stops + 1))

        return -1

