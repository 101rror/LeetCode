class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def dfs(start, hashset):
            if start == n:
                return 0

            maxsplit = 0

            for end in range(start + 1, n + 1):
                substr = s[start : end]

                if substr not in hashset:
                    hashset.add(substr)
                    maxsplit = max(maxsplit, 1 + dfs(end, hashset))
                    hashset.remove(substr)

            return maxsplit

        return dfs(0, set())