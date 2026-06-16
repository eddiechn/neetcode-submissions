class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        area = (r - l) * min(h[l], h[r])
        update a var
        """

        l = 0
        r = len(heights) - 1

        res = 0
        while l <= r:
            local = (r - l) * min(heights[l], heights[r])
            res = max(local, res)

            if heights[r] < heights[l]:
                r -= 1

            else:
                l += 1


        return res

        