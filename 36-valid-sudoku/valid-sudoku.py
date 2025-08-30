class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                number = str(board[i][j])

                if number != ".":
                    row = number + "in row" + str(i)
                    col = number + "in col" + str(j)
                    block = number + "in block" + str(i // 3) + str(j // 3)

                    if row in seen or col in seen or block in seen:
                        return False

                    seen.add(row)
                    seen.add(col)
                    seen.add(block)

        return True
