class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1

        w = 0 
        while up <= down:
            mid = up + (down - up) // 2
            if target < matrix[mid][0]:
                down = mid - 1

            elif target > matrix[mid][-1]:
                up = mid + 1

            else:
                w = mid
                break


        while l <= r:
            m = l + (r - l) // 2
            if target < matrix[w][m]:
                r = m - 1
            elif target > matrix[w][m]:
                l = m + 1

            else:
                return True


        return False

        