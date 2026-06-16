class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def countPal( s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[r] == s[l]:
                res += 1
                l -= 1
                r += 1

            return res

        for i in range(len(s)):
            res += countPal(s, i, i)
            res += countPal(s, i, i + 1)

        return res





        
       
        