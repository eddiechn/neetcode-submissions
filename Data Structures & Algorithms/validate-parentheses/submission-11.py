class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{":"}", "[":"]"}

        stack = []




        for c in s:
            if c in brackets:
                stack.append(c)
                

            else:
                if not stack:
                    return False
                if c != brackets[stack.pop()]:
                    return False


        return True if not stack else False
        