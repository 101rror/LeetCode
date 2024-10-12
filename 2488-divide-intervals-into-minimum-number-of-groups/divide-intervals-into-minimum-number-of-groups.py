class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []

        for left, right in intervals:
            if heap:
                if heap[0] < left:
                    heappop(heap)
            heappush(heap, right)

        return len(heap)