class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')] += 1


        count.sort()
        maxF = count[25]
        idleSpots = (maxF - 1) * n

        for i in range(24, -1, -1):
            idleSpots -= min(maxF - 1, count[i])

        return max(0, idleSpots)  + len(tasks)       