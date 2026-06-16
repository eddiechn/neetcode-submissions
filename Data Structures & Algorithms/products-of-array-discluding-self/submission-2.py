class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for n in nums:
            if n:
                product *= n
            else:
                zero += 1

        if zero > 1 :
            return [0] * len(nums)

        res = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            if zero:
                if nums[i]:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product // nums[i]


        return res


        