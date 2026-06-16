class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(i, x, cur):
            if x == target:
                res.append(cur.copy())
                return
            if x > target or i >= len(nums):
                return

            cur.append(nums[i])
            backtrack(i, x + nums[i], cur)

            cur.pop()
            backtrack(i + 1, x, cur)


        backtrack(0, 0, [])

        return res
        