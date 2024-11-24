class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        tsum = 0
        mn = float("inf")
        neg = 0

        for row in matrix:
            for val in row:
                if val < 0:
                    neg += 1

                tsum += abs(val)
                mn = min(mn, abs(val))
                

        return (tsum - 2 * mn) if neg % 2 != 0 else tsum