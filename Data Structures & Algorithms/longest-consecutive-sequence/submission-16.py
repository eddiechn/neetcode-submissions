class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            
            if n - 1 not in nums:
                local = 1
                while n + local in nums:
                    local += 1


                res = max(res, local)


        return res
        