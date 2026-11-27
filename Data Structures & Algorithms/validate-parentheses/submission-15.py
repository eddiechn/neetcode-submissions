class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{": "}", "(": ")", "[": "]"}

        stack = []

        for c in s:
            if c not in brackets:
                if not stack:
                    return False
                if c != brackets[stack.pop()]:
                    return False


            if c in brackets:
                stack.append(c)




        return not stack
        