class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for n in nums:
                if n not in subset:
                    subset.append(n)
                    backtrack(subset)
                    subset.pop()

            

        backtrack([])

        return res