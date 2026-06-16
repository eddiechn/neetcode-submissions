class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s + "."

        return encoded
        

    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        for c in s:
            if c == ".":
                res.append(cur)
                cur = ""
            else:
                cur += c
 


        return res

                    
