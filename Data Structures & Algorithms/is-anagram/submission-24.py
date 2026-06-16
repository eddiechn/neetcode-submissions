class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        if len(t) != len(s):
            return False


        for n in range(len(s)):
            count[ord(s[n]) - ord('a')] += 1
            count[ord(t[n]) - ord('a')] -= 1


        for n in count:
            if n != 0:
                return False


        return True
        