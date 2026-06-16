class Solution {
    public int findMin(int[] nums) {

        // O(logn) binary search : has to be sorted 

        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {

            if (nums[left] <= nums[right]) {
                return nums[left];
            }

            int mid = (left + right) / 2;

            if (nums[left] <= nums[mid]) {
                left = mid + 1;
            } else {
                right = mid;

            }

        }

        return 0;
        
    }
}
