class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(-s)

        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first < second:
                heapq.heappush(heap, first - second)


        return abs(heap[0]) if heap else 0

            

        