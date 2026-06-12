class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = n.bit_length()

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        dep = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]

        q = deque([1])
        vis = [False] * (n + 1)
        vis[1] = True

        while q:
            u = q.popleft()
            for v in g[u]:
                if not vis[v]:
                    vis[v] = True
                    dep[v] = dep[u] + 1
                    up[v][0] = u
                    for j in range(1, LOG):
                        up[v][j] = up[up[v][j - 1]][j - 1]
                    q.append(v)

        def lca(a, b):
            if dep[a] < dep[b]:
                a, b = b, a

            k = dep[a] - dep[b]
            for j in range(LOG):
                if k >> j & 1:
                    a = up[a][j]

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if up[a][j] != up[b][j]:
                    a = up[a][j]
                    b = up[b][j]

            return up[a][0]

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            w = lca(u, v)
            d = dep[u] + dep[v] - 2 * dep[w]
            ans.append(pow(2, d - 1, MOD))

        return ans
