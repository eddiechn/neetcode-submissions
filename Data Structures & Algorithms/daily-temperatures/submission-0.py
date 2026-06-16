class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for tempId, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i, t = stack.pop()
                res[i] = tempId - i

                
                

            stack.append([tempId, temp])


        return res



        
        