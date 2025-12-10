class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        fi = complexity[0]

        for c in complexity[1:]:
            if c <= fi:
                return 0

        fact = 1
        for i in range(2, n):
            fact = fact * i

        return fact % MOD
