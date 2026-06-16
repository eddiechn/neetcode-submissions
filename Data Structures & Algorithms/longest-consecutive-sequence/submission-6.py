class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        current = 0
        for n in nums:
            
            if (n - 1) not in nums:
                current = 1
                while n + current in nums:
                    current += 1

            res = max(current, res)


        return res
        