class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n, q = len(heights), len(queries)
        ans = [-1] * q
        deferred = [[] for _ in range(n)]
        pq = []

        for i in range(q):
            a, b = queries[i]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                deferred[b].append((heights[a], i))

        for i in range(n):
            for query in deferred[i]:
                heapq.heappush(pq, query)
            while pq and pq[0][0] < heights[i]:
                ans[pq[0][1]] = i
                heapq.heappop(pq)

        return ans