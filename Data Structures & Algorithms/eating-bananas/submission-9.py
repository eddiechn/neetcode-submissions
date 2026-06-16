class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        going through all possible speeds
        """
        l = 1
        r = max(piles)
        k = 0


        while l <= r:
            mid = l + (r - l) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / mid)

            if time > h:
                l = mid + 1

            else:
                k = mid
                r = mid - 1


        return k


        