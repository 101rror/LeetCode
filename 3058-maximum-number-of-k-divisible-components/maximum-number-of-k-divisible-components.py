class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k) -> int:
        if n == 1:
            return 1
        count = 0
        mp = defaultdict(set)
        
        for u, v in edges:
            mp[u].add(v), mp[v].add(u)

        queue = deque(u for u, vs in mp.items() if len(vs) == 1)

        while queue:
            for _ in range(len(queue)):
                u = queue.popleft()

                p = next(iter(mp[u])) if mp[u] else -1
                if p >= 0:
                    mp[p].remove(u)

                if values[u] % k == 0:
                    count += 1
                else:
                    values[p] += values[u]

                if p >= 0 and len(mp[p]) == 1:
                    queue.append(p)

        return count
