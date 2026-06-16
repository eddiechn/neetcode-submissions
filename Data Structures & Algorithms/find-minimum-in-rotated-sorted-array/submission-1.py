
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:  # Use l < r to avoid unnecessary comparisons
            # If the array is sorted or single element is left
            if nums[l] <= nums[r]:
                return nums[l]

            mid = (l + r) // 2
            
            # If left part is sorted, pivot must be in the right part
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:  # Pivot is in the left part
                r = mid

        # At the end, l == r, pointing to the smallest element
        return nums[l]
