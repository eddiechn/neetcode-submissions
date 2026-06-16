class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int curSum = numbers[left] + numbers[right];

            if (target < curSum) {
                right--;
            } else if (target > curSum) {
                left++;
            } else {
                return new int[] {left+1, right+1};
            }
        }  

        return new int[] {};
    
    }
}
