class Solution:
    def countArrays(self, original: list[int], bounds: list[list[int]]) -> int:
        n = len(original)
        left, right = bounds[0]

        for i in range(1, n):
            diff = original[i] - original[i - 1]

            left = max(left + diff, bounds[i][0])
            right = min(right + diff, bounds[i][1])

            if left > right:
                return 0

        return right - left + 1
