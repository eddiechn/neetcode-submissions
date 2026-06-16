class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0
        while l <= r:
            s = l + (r - l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / s)

            if time <= h:
                res = s
                r = s - 1

            else:
                l = s + 1


        return res


        