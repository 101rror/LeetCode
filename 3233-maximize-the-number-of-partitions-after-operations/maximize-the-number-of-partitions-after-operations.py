from functools import lru_cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def cnt(n: int) -> int:
            return bin(n).count("1")

        @lru_cache(None)
        def dfs(i, mask, used):
            if i >= len(s):
                return 1

            ans = 0

            if not used:
                for j in range(1, 26):
                    msk = mask | (1 << j)
                    if cnt(msk) <= k:
                        ans = max(ans, dfs(i + 1, msk, True))
                    else:
                        ans = max(ans, 1 + dfs(i + 1, (1 << j), True))

            bit = 1 << (ord(s[i]) - 97)
            msk = mask | bit
            if cnt(msk) <= k:
                ans = max(ans, dfs(i + 1, msk, used))
            else:
                ans = max(ans, 1 + dfs(i + 1, bit, used))

            return ans

        return dfs(0, 0, False)
