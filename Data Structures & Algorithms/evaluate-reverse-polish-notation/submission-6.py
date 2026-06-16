class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        ops = ["*", "+", "-", "/"]
        for t in tokens:
            if t not in ops:
                stack.append(int(t))

            else:
                if t == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)

                elif t == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)

                elif t == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)

                elif t == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))

        return stack[-1]
        