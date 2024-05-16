class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        tsum = 0
        for i in range(len(s)):
            tsum += abs(s.index(s[i]) - t.index(s[i]))

        return tsum