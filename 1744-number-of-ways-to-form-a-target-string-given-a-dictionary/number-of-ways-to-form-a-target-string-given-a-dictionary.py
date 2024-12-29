class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        counter = list(map(Counter, zip(*map(list, words))))

        for char in counter:
            for i in reversed(range(n)):
                dp[i + 1] += dp[i] * char[target[i]] % mod
                dp[i + 1] %= mod

        return dp[n]
