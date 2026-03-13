class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        pq = []
        ans = 0

        for time in workerTimes:
            heappush(pq, (time, time, 1))

        for _ in range(mountainHeight):
            currentTime, originalTime, iteration = heappop(pq)
            ans = currentTime

            heappush(pq, (currentTime + originalTime * (iteration + 1), originalTime, iteration + 1))

        return ans
        