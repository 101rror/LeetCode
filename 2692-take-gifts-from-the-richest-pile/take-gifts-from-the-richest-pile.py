class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for gift in gifts:
            heap.append(-gift)

        heapq.heapify(heap)

        while(k):
            large = -heappop(heap)
            sqt = int(large ** 0.5)
            heappush(heap, -sqt)
            k -= 1

        return abs(sum(heap))
