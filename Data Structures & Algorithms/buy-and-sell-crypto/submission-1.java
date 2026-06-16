class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxDiff = 0;

        while (right < prices.length ) {
            if (prices[left] < prices[right]) {
                maxDiff = Math.max(maxDiff, prices[right] - prices[left]);
                
                
            }

            else left = right;

            right++;
        }
        
        return maxDiff;
        
    }
}
