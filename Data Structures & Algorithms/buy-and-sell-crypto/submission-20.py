class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        res = 0
        while r < len(prices):
            if prices[r] >= prices[l]:
                res = max(res, prices[r] - prices[l])
                r += 1

            else:
                l = r


        return res
            

        