class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
                    break

        ans = 0

        for i in range(x - 1, -1, -1):
            if board[i][y] == "p":
                ans += 1
                break
            if board[i][y] == "B":
                break

        for i in range(x + 1, 8):
            if board[i][y] == "p":
                ans += 1
                break
            if board[i][y] == "B":
                break

        for i in range(y - 1, -1, -1):
            if board[x][i] == "p":
                ans += 1
                break
            if board[x][i] == "B":
                break

        for i in range(y + 1, 8):
            if board[x][i] == "p":
                ans += 1
                break
            if board[x][i] == "B":
                break


        return ans