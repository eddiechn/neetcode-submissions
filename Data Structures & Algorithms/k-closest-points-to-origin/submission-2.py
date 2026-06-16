class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []

        for x, y in points:
            distances.append([math.sqrt(x**2 + y**2), x, y])

        heapq.heapify(distances)
        res = []
        while len(res) < k:
            d, x, y = heapq.heappop(distances)
            res.append([x, y])


        return res
        


        # res = []
        # while len(res) != k:
        #     res.append(heapq.heapify)




        