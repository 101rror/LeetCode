class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        dp = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if dp[pa] < dp[pb]:
                parent[pa] = pb
            elif dp[pb] < dp[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                dp[pa] += 1

        for u, v in allowedSwaps:
            union(u, v)

        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        ans = 0

        for indices in groups.values():
            freq = Counter()

            for idx in indices:
                freq[source[idx]] += 1

            for idx in indices:
                if freq[target[idx]] > 0:
                    freq[target[idx]] -= 1
                else:
                    ans += 1

        return ans