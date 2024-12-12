class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for gift in gifts:
            heap.append(-gift)

        heapq.heapify(heap)

        while k:
            top = -heapq.heappop(heap)
            sqt = int(sqrt(top))
            heapq.heappush(heap, -sqt)
            k -= 1

        ans = 0

        for gift in heap:
            ans += (-1 * gift)

        return ans