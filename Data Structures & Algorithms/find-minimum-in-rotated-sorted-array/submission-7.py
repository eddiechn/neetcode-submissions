class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        1, 2, 3, 4, 5, 6
        
        4, 5,  1, 2, 3 -> obv the minimum is 1

        we want to find the window in which the minimum is
        find the turnaround, the rotation

        two pointers, l, r
        if l < mid:
            then obviously, the minimum is in there. 
            we can move l to mid, check again. if still l > r;
            then move l to mid. 

            if r > l, then we have found the start of the window

        """

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            mid = l + (r - l ) // 2
            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid


        return nums[l]


        


        