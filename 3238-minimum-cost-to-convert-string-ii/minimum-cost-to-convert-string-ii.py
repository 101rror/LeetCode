class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)

        idx = dict()
        for s in original + changed:
            if s not in idx:
                idx[s] = len(idx)
        K = len(idx)

        dist = [[math.inf] * K for _ in range(K)]
        for o, c, w in zip(original, changed, cost):
            u, v = idx[o], idx[c]
            dist[u][v] = min(dist[u][v], w)

        for k in range(K):
            for u in range(K):
                if dist[u][k] != math.inf:
                    for v in range(K):
                        if (dist[k][v] != math.inf and dist[u][k] + dist[k][v] < dist[u][v]):
                            dist[u][v] = dist[u][k] + dist[k][v]

        lengths = set(map(len, original))

        dp = [0] + [math.inf] * n
        for i in range(n):
            if dp[i] == math.inf:
                continue

            if target[i] == source[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for l in lengths:
                if i + l >= len(dp):
                    continue

                u = idx.get(source[i : i + l], -1)
                v = idx.get(target[i : i + l], -1)
                if u >= 0 and v >= 0:
                    dp[i + l] = min(dp[i + l], dp[i] + dist[u][v])

        return dp[-1] if dp[-1] != math.inf else -1
