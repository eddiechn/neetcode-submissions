class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            distances.append([d, x, y])

        heapq.heapify(distances)

        res = []
        while len(res) < k:
            d, x, y = heapq.heappop(distances)
            res.append([x, y])


        return res
        