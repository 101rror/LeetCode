class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        arr = [[] for _ in range(n)]
        res = 0

        for i in range(n):
            if (manager[i] != -1):
                arr[manager[i]].append(i)

        q = deque([(headID, informTime[headID])])

        while q:
            size = len(q)

            for _ in range(size):
                t = q.popleft()

                for x in arr[t[0]]:
                    if (informTime[x] == 0):
                        res = max(res, t[1])
                    else:
                        q.append((x, t[1] + informTime[x]))

        return res