class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x == y:
                continue
            
            elif x > y:
                heapq.heappush(stones, y - x)


        return abs(stones[-1]) if stones else 0


        