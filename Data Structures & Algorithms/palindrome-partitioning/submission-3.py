class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return 

            for j in range(i, len(s)):
                if self.palindrome(s[i:j + 1]):
                    cur.append(s[i:j + 1])
                    dfs(j + 1, cur)
                    cur.pop()

        dfs(0, [])
        return res




    def palindrome(self, word):
        l = 0
        r = len(word) -1
        
        while l < r:
            if word[l] != word[r]:
                return False

            l += 1
            r -= 1

        return True
        