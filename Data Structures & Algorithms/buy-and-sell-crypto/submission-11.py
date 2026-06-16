class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        r = l + 1

        while r < len(prices):
            res = max(prices[r] - prices[l], res)

            if prices[r] < prices[l]:
                l = r
            else: 
                r += 1

        return res

        