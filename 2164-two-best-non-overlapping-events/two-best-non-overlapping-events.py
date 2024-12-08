class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pre, maxvalue = 0, 0
        heap = []

        for start, end, value in events:
            while heap and heap[0][0] < start:
                pre = max(pre, heapq.heappop(heap)[1])

            maxvalue = max(maxvalue, pre + value)
            heapq.heappush((heap), (end, value))

        return maxvalue
