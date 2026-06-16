class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        if not heights:
            return 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                local = min(heights[i:j + 1]) * (j - i + 1)
                res = max(local, res)


        return res