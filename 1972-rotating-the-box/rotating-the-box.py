class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row = len(boxGrid)
        col = len(boxGrid[0])

        ans = [["."] * row for _ in range(col)]

        for k, v in enumerate(boxGrid):
            btm = col - 1
            for j in range(col - 1, -1, -1):
                if v[j] == "#":
                    ans[btm][row - 1 - k] = "#"
                    btm -= 1
                elif v[j] == "*":
                    ans[j][row - 1 - k] = "*"
                    btm = j - 1

        return ans
