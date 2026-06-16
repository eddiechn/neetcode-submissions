class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        res = 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            res = max(res, diff)

            if diff < 0:
                l = r

            else:
                r += 1

            

        return res
            

        

        