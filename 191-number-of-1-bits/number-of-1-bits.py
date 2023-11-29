class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = bin(n).count('1')

        return ans