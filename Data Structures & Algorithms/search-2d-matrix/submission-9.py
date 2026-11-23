class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1


        current = 0

        while up <= down:
            mid = up + (down - up) // 2

            if target > matrix[mid][-1]:
                up = mid + 1

            elif target < matrix[mid][0]:
                down = mid - 1

            else:
                current = mid
                break


        while left <= right:
            mid = right + (left - right) // 2

            if target > matrix[current][mid]:
                left = mid + 1

            elif target < matrix[current][mid]:
                right = mid - 1

            else:
                return True



        return False

        