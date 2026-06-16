class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # first node - you only want to take the cheapest one
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
                for nei, price in graph[node]:
                    heapq.heappush(heap, (cost + price, nei, stops + 1))
        
        return -1