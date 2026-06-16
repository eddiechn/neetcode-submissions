class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def bt(i, local, subset):
            if local == target:
                res.append(subset.copy())
                return

            if local >= target or i >= len(candidates):
                return

            subset.append(candidates[i])
            bt(i + 1, local + candidates[i], subset)
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: 
                i += 1
                
            bt(i + 1, local, subset)


        bt(0, 0, [])
        return res