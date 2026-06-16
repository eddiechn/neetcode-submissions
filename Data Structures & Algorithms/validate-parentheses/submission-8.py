class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []


        for c in s:
            if c in brackets:
                stack.append(c)
            elif not stack or c != brackets[stack.pop()]:
                return False

        return not stack
        