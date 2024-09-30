class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        i0 = i1 = i2 = i3 = -inf
        a0, a1, a2, a3 = a

        for num in b:
            i3 = max(i3, i2 + a3 * num)
            i2 = max(i2, i1 + a2 * num)
            i1 = max(i1, i0 + a1 * num)
            i0 = max(i0, a0 * num)

        return i3