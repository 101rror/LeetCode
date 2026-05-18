class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        mp = defaultdict(list)

        for i, x in enumerate(arr):
            mp[x].append(i)

        q = deque([(0, 0)])
        visited = {0}

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            nxt = mp[arr[i]] + [i - 1, i + 1]

            for j in nxt:
                if 0 <= j < n and j not in visited:
                    visited.add(j)
                    q.append((j, steps + 1))

            mp[arr[i]].clear()

        return -1
