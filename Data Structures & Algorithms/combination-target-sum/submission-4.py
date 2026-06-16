class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(i, cur, l):

            if cur == target:
                res.append(l.copy())
                return

            if cur > target or i >= len(nums):
                return

            l.append(nums[i])
            backtrack(i, cur + nums[i], l)
            l.pop()
            backtrack(i + 1, cur, l)


        backtrack(0, 0, [])

        return res
        