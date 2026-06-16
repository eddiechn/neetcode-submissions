class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []


        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                i2, t2 = stack.pop()
                res[i2] = i - i2
            stack.append([i, t])

        return res
        