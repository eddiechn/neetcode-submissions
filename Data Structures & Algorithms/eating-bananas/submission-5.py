class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        res = max(piles)

        l = 1
        r = res


        while l <= r:
            mid = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / mid)
            if total <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

            



        


        