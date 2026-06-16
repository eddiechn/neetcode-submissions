class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i1, t1 in enumerate(temperatures):
            while stack and stack[-1][1] < t1:
                i2, t2 = stack.pop()
                result[i2] = i1 - i2

            stack.append((i1, t1))



        return result


    




        