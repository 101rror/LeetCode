class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if (numRows   == 0):
            return []
        elif (numRows == 1):
            return [[1]]
        ans = [[1]]

        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(ans[i - 1][j - 1] + ans[i - 1][j]) 
            row.append(1)
            ans.append(row)
        return ans