class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0

        l = 0
        r = 0

        for i in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            r += 1

            res = max(res, r - l)

        return res
        


   
            




        
        