class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(c, o, cur):
            if c == o == n:
                res.append("".join(cur))


            if o < n:
                dfs(c, o + 1, cur + ['('])

            if c < o:
                dfs(c + 1, o, cur + [')'])


        dfs(0, 0, [])

        return res
        