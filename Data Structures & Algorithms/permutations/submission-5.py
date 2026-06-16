class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return


            for n in nums:
                if n not in cur:
                    cur.append(n)
                    bt(cur)
                    cur.pop()


        bt([])
        return res
        