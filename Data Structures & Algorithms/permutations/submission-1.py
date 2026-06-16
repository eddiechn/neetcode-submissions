class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []

        def dfs():
            
            # base case
            if len(subset) == len(nums):
                res.append(subset.copy())
                return 

            for n in nums:
                if n not in subset:
                    subset.append(n)
                    dfs()
                    subset.pop()

        dfs()

        return res

            







            

        