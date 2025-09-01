class Solution:
    def maxAverageRatio(self, classes: List[List[int]], k: int) -> float:
        n = len(classes)
        tsum = 0
        heap = []

        for p, q in classes:
            tsum += p / q
            heap.append(((p - q) / (q * (q + 1)), p, q))

        heapify(heap)

        for _ in range(k):
            (r, p, q) = heap[0]
            if r == 0:
                break
            tsum -= r
            x = (p - q) / ((q + 1.0) * (q + 2.0))
            heapreplace(heap, (x, p + 1, q + 1))

        return tsum / n
