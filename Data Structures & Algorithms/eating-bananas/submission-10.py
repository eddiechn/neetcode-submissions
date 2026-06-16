class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0

        while l <= r:
            m = (r + l ) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / m)

            if time > h:
                l = m + 1

            else:
                k = m
                r = m - 1


        return k