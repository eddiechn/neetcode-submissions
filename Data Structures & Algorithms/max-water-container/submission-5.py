class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        area = 0

        while left < right:
            curr = min(heights[left], heights[right]) * (right - left)
            area = max(area, curr)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1


        return area
