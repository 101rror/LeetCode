import heapq


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[py] = px
        return True


class Solution:
    def processQueries(
        self, n: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        dsu = DSU(n)
        online = [True] * (n + 1)

        for u, v in connections:
            dsu.union(u, v)

        component_heap = defaultdict(list)
        for station in range(1, n + 1):
            root = dsu.find(station)
            heapq.heappush(component_heap[root], station)

        ans = []

        for typ, x in queries:
            if typ == 2:
                online[x] = False
            else:
                if online[x]:
                    ans.append(x)
                else:
                    root = dsu.find(x)
                    heap = component_heap[root]
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)
                    ans.append(heap[0] if heap else -1)

        return ans
