class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxPrices = 0
        l = 0
        r = l + 1


        while r < len(prices):
            local = prices[r] - prices[l]
            
            maxPrices = max(maxPrices, local)


            if prices[r] < prices[l]:
                l = r


            else:

                r += 1


        return maxPrices
        