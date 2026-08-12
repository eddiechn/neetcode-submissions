class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        start of string - number of letters - string
        """
        res = ""
        for s in strs:
            n = len(s)
            res += str(n)
            res += "#"
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1


            strlen = int(s[i:j])
            i = j + 1
            j = i + strlen
            res.append(s[i:j])

            i = j

        return res

