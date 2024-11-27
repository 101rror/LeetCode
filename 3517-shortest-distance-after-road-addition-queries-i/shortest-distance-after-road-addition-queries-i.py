class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}

        for i in range(n - 1):
            graph[i].append((i + 1, 1))
        
        def dfs():
            dis = [float('inf')] * n
            dis[0] = 0
            dp = [(0, 0)]

            while dp:
                cur , u = heapq.heappop(dp)
                if cur < dis[u]:
                    continue
                for v, w in graph[u]:
                    d = cur + w
                    if d < dis[v]:
                        dis[v] = d
                        heapq.heappush(dp, (d, v))

            return dis[n - 1]

        ans = []

        for u, v in queries:
            graph[u].append((v, 1))
            check = dfs()
            ans.append(check)

        return ans
