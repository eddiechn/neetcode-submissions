class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, local):

            if local == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or local > target:
                return

            subset.append(nums[i])
            dfs(i, local + nums[i])

            subset.pop()
            dfs(i + 1, local)


        dfs(0, 0)
        return res

      

            
