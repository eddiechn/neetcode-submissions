class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, o, c):
            if n == o == c:
                res.append("".join(cur))
                return

            if o < n:
                dfs(cur + ['('], o + 1, c)
            
            if c < o:
                dfs(cur +  [')'], o, c + 1)

        dfs([], 0, 0)
        return res


        