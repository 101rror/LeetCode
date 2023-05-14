class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        n = len(matrix)
        m = len(matrix[0])
        first = 0
        last = n * m - 1
        
        while (first <= last):
            mid = (first + last) // 2
            x = (mid // m)
            y = (mid % m)

            if (matrix[x][y] == target):
                return True
            if (target > matrix[x][y]):
                first = mid + 1
            else:
                last = mid - 1
        return False