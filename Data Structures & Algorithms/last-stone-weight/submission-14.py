class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heap = stones
        heapq.heapify(heap)


        while len(stones) > 1:

            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x == y:
                continue

            if x < y:
                heapq.heappush(heap, x - y)


        return -stones[0] if stones else 0



        