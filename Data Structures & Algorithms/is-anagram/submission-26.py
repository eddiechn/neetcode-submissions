class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        if len(s) != len(t):
            return False

        for n in range(len(s)):
            count[ord(s[n]) - ord('a')] += 1
            count[ord(t[n]) - ord('a')] -= 1

        
        for t in count:
            if t != 0:
                return False


        return True
        