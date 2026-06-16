class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        r = l + 1

        while r < len(prices):
            local = prices[r] - prices[l]
            res = max(res, local)

            if prices[l] > prices[r]:
                l = r

            r += 1


        return res
        