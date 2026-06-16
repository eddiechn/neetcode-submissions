class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            local = 1
            if n - 1 not in nums:
                while n + local in nums:
                    local += 1

            res = max(res, local)
  


        return res

        