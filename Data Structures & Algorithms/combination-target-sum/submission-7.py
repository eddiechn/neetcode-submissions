class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, s, i):
            if s == target:
                res.append(cur.copy())
                return 

            if i >= len(nums):
                return

            if s > target:
                return

            cur.append(nums[i])
            dfs(cur, s + nums[i], i)
            cur.pop()
            dfs(cur, s, i + 1)


        dfs([], 0, 0)

        return res       