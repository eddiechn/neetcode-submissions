class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []


        cars = []
        for p, s in zip(position, speed):
            cars.append((p, s))

        cars.sort(reverse=True)

        for p, s in cars:
            time = (target - p) / s
            if stack and stack[-1] >= time:
                continue

            stack.append(time)


        return len(stack)
  
