class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,  1
        res = 0
        while r < len(prices):
            local = prices[r] - prices[l]

            if prices[l] <= prices[r]:
                r += 1
                res = max(res, local)
            else:
                l = r
        return res    