class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def dfs(i, cur, s):
            if s == target:
                res.append(cur.copy())
                return 
            if i >= len(candidates):
                return 

            if s > target:
                return 

    


            dfs(i + 1, cur + [candidates[i]], s + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, s)


        dfs(0, [], 0)
        return res
        