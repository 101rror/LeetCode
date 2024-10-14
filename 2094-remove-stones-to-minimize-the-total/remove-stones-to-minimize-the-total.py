class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []

        for pile in piles:
            heap.append(-pile)

        heapq.heapify(heap)

        while(k):
            large = -heappop(heap)
            if (large % 2 != 0): heappush(heap, -floor(large / 2) - 1)
            else : heappush(heap, -floor(large / 2))
            k -= 1

        return abs(sum(heap))