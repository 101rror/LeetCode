class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def dfs(i, j, visited):
            if (i < 0 or j < 0 or i == row or j == col or (i, j) in visited):
                return 0
            if (i == row - 1):
                return 1

            visited.add((i, j))
            return dfs(i, j+1, visited)|dfs(i, j-1, visited)|dfs(i+1, j, visited)|dfs(i-1, j, visited)

        left = 0
        right = len(cells) - 1

        while (left <= right):
            mid = (left+right)//2
            visited = set()

            for i in range(mid+1):
                visited.add((cells[i][0]-1, cells[i][1]-1))
            result = False

            for j in range(col):
                if dfs(0, j, visited):
                    result = True
                    break

            if result:
                left = mid + 1

            else:
                right = mid - 1

        return left