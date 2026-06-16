class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod  = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                prod *= num

            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_count == 1:
                res[i] = 0 if c != 0 else prod
                
            else:
                res[i] = prod // c


        return res




        
        
        