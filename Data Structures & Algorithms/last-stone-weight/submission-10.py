class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones

        heapq.heapify_max(self.heap)

        while len(self.heap) > 1:

            first = heapq.heappop_max(self.heap)
            second = heapq.heappop_max(self.heap)

            if first == second:
                continue
            else:
                difference = first - second
                heapq.heappush_max(self.heap, difference)


        return self.heap[0] if self.heap else 0

            
        

        
        