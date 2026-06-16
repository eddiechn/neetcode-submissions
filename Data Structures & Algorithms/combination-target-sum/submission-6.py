class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(cur, total, i):
            if total > target or i >= len(nums):
                return 
            if total == target:
                res.append(cur.copy())
                return

            
            cur.append(nums[i])
            backtrack(cur, total + nums[i], i)
            cur.pop()
            backtrack(cur, total, i + 1)


        backtrack([], 0, 0)
        return res
        