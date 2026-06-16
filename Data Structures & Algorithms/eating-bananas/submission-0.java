class Solution {
    public int minEatingSpeed(int[] piles, int h) {

    

        int left = 1;
        int right = Arrays.stream(piles).max().getAsInt();

        int result = right;

        while (left <= right) {
            int k = (left+right)/2;
            if (canEat(piles, k, h)) {
                result = k;
                right = k - 1;
            } else {
                left = k+1;
            }
        }

        return result;
        

        
    }


    private boolean canEat(int[] piles, int k, int h) {
        int numberHours = 0;

        for (int pile : piles) {
            numberHours += (pile / k);
            if (pile % k != 0) numberHours++;
        }
        return numberHours <= h;
    } 
}
