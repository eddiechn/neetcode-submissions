class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        api = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl", 
            6: "mno", 
            7: "pqrs", 
            8: "tuv", 
            9: "wyxz" 
        }

        res = []
        def dfs(cur, i):
            if len(cur) == len(digits):
                res.append(cur)
                return

            for c in api[int(digits[i])]:
                dfs(cur + c, i + 1)

        if digits:

            dfs("", 0)

        return res