class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1

        res = 0


        while r < len(prices):
            local = prices[r] - prices[l]
            
            if prices[l] > prices[r]:
                l = r

            res = max(res, local)
            r += 1


        return res
        