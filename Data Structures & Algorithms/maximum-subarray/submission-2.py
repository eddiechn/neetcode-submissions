class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        c = 0

        for n in nums:
            if c < 0:
                c = 0
            c += n
            res = max(res, c)


        return res
        