class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        res = 0

        while r < len(prices):

            if prices[r] < prices[l]:
                l = r

            else:
                local = prices[r] - prices[l]
                res = max(res, local)

                r += 1


        return res

        