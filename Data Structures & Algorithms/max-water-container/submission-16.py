class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            local = (r - l) * min(heights[l], heights[r])

            res = max(local, res)
            
            if heights[l] <= heights[r]:
                l += 1

            else:
                r -= 1


        return res

            


                