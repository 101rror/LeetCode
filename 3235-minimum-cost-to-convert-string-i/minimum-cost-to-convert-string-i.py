class Solution:
    def find(self, graph, x, y, d):
        if (x, y) in d:
            return d[(x, y)]
        pq, visit = [], set()
        heapq.heappush(pq, (0, x))

        while pq:
            cost, node = heapq.heappop(pq)
            if node in visit:
                continue
            if node == y:
                return cost
            visit.add(node)
            for nei, nCost in graph[node]:
                heapq.heappush(pq, (cost + nCost, nei))

        return -1

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        graph = defaultdict(list)

        for x, y, z in zip(original, changed, cost):
            graph[x].append([y, z])

        ans, d = 0, {}
        for i in range(n):
            val = self.find(graph, source[i], target[i], d)
            if val == -1:
                return -1
            else:
                ans += val
            d[(source[i], target[i])] = val

        return ans
