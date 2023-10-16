from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if(rowIndex < 0):
            return []

        ans = [1]

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                if(j == i):
                    ans.append(1)
                else:
                    ans[j] = ans[j] + ans[j - 1]

        return ans