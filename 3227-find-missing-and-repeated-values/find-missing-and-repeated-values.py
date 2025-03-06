class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        res = []

        for i in grid:
            for j in i:
                ans.append(j)

        ast = list(set(ans))
        x = 0

        for i in ast:
            if ans.count(i) > 1:
                res.append(i)
        for i in range(1, len(ast)):
            if abs(ast[i - 1] - ast[i]) != 1:
                x = ast[i] - 1

        if x == 0 and ast[0] == 1:
            res.append(ast[len(ast) - 1] + 1)
        elif x == 0 and ast[0] != 1:
            res.append(ast[0] - 1)
        else:
            res.append(x)

        return res
