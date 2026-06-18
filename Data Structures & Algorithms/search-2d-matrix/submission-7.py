class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        row = 0

        while t <= b:
            mid = (b - t) // 2 + t
            if target < matrix[mid][0]:
                b = mid - 1

            elif target > matrix[mid][-1]:
                t = mid + 1

            else:
                row = mid
                break

        while l <= r:
            mid = (r - l) // 2 + l 
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1

            else:
                return True


        return False
