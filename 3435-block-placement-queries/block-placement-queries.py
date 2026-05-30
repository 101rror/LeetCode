class Solution:
    def __init__(self):
        self.MAXI = 50000
        self.seg = [0] * (4 * (self.MAXI + 1))

    def update(self, node, l, r, idx, val):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)

        self.seg[node] = max(self.seg[2 * node], self.seg[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if qr < l or ql > r:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(self.query(2 * node, l, mid, ql, qr), self.query(2 * node + 1, mid + 1, r, ql, qr))

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        from sortedcontainers import SortedSet
        barriers = SortedSet([0])

        for q in queries:
            if q[0] == 1:
                barriers.add(q[1])

        positions = list(barriers)

        for i in range(1, len(positions)):
            self.update(1, 0, self.MAXI, positions[i], positions[i] - positions[i - 1])

        ans = []

        for i in range(len(queries) - 1, -1, -1):
            if queries[i][0] == 2:
                x = queries[i][1]
                sz = queries[i][2]

                idx = barriers.bisect_right(x) - 1
                prevBarrier = barriers[idx]

                bestGap = self.query(1, 0, self.MAXI, 0, prevBarrier)
                bestGap = max(bestGap, x - prevBarrier)

                ans.append(bestGap >= sz)

            else:
                x = queries[i][1]
                idx = barriers.index(x)
                leftBarrier = barriers[idx - 1]
                self.update(1, 0, self.MAXI, x, 0)

                if idx + 1 < len(barriers):
                    rightBarrier = barriers[idx + 1]

                    self.update(1, 0, self.MAXI, rightBarrier, rightBarrier - leftBarrier)

                barriers.remove(x)

        ans.reverse()

        return ans
