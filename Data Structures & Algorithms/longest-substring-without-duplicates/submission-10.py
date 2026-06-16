class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1

        seen = set()
        if not s:
            return 0
        seen.add(s[l])
        res = 1

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            r += 1

            res = max(res, r - l)


        return res
            

        