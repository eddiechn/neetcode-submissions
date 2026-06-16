class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nrows = len(matrix)
        ncols = len(matrix[0])

        top = 0
        bottom = nrows - 1


        while top <= bottom: 
            middle = (top + bottom) // 2

            if target > matrix[middle][-1]:
                top = middle + 1

            elif target < matrix[middle][0]:
                bottom = middle - 1

            else:
                break

        mid = (top + bottom) // 2

        left = 0
        right = ncols - 1

        while left <= right:
            middle = (left + right) // 2

            if target < matrix[mid][middle]:
                right = middle - 1

            elif target > matrix[mid][middle]:
                left = middle + 1


            else:
                return True

        return False
                

        