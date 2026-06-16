class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])
        up, down = 0, nrows - 1


        while up <= down:
            mid = (up + down) // 2
            if target > matrix[mid][ncols-1]:
                up = mid + 1
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                break

        row = (up + down) // 2
        l, r = 0, ncols  - 1
        while (l <= r):
            mid = (l + r) // 2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1

            else:
                return True

        return False
                

            


        