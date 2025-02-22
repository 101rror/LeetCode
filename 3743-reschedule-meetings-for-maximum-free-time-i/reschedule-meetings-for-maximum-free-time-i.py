class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        free = [0] * n
        free[0] = startTime[0] - 0

        for i in range(1, n):
            free[i] = startTime[i] - endTime[i - 1]
        free.append(eventTime - endTime[-1])

        if max(free) == 0:
            return 0

        maxm = csum = sum(free[: k + 1])

        for i in range(k + 1, len(free)):
            csum += free[i] - free[i - k - 1]
            maxm = max(maxm, csum)

        return maxm
