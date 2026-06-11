class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = int(1e9) + 7
        dct = defaultdict(list)

        for u, v in edges:
            dct[u].append(v)
            dct[v].append(u)

        mx = [0]

        def dfs(node, parent, cur):
            if cur > mx[0]:
                mx[0] = cur
            for nei in dct[node]:
                if nei == parent:
                    continue
                dfs(nei, node, cur + 1)

        dfs(1, -1, 0)

        return 1 if mx[0] == 0 else pow(2, mx[0] - 1, MOD)
