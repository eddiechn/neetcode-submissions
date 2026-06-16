class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["*", "+", "-", "/"]
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                a = stack.pop()
                a = int(a)
                b = stack.pop()
                b = int(b)

                if t == "*":
                    res = a * b
                    stack.append(res)
                
                elif t == "/":
                    res = int(b / a)
                    stack.append(res)

                elif t == "+":
                    res = a + b
                    stack.append(res)

                elif t == "-":
                    res = b - a
                    stack.append(res)
        

        return int(stack[-1])

        