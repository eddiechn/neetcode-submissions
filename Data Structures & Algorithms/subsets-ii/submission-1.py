class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(cur, i):
            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(cur, i + 1)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(cur, i + 1)

        dfs([], 0)
        return res

        