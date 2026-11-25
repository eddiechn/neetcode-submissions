class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        sqrt((x1 - x2)**2 + (y1 - y2)**2)
        """

        distances = []
        heapq.heapify(distances)

        for x, y in points:
            distance = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(distances, [distance, x, y])

        res = []

        while len(res) < k:
            d, x, y = heapq.heappop(distances)
            res.append([x, y])


        return res

        