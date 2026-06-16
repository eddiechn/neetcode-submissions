class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        local = 0
        for n in nums:
            if n - 1 not in nums:
                local = 1
                while n + 1 in nums:
                    local += 1
                    n += 1

            res = max(local, res)



        return res