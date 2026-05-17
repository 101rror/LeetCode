class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        q = deque([start])

        while q:
            for _ in range(len(q)):
                val = q.popleft()
                if val in visited:
                    continue
                visited.add(val)

                if arr[val] == 0:
                    return True

                if val + arr[val] < n:
                    if arr[val + arr[val]] == 0:
                        return True
                    q.append(val + arr[val])
                if val - arr[val] > -1:
                    if arr[val - arr[val]] == 0:
                        return True
                    q.append(val - arr[val])

        return False
