class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        tsum, neg, mn = 0, 0, float("inf")

        for row in matrix:
            for val in row:
                if val < 0:
                    neg += 1

                tsum += abs(val)
                mn = min(mn, abs(val))

        return (tsum - 2 * mn) if neg & 1 else tsum
