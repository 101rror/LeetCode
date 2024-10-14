class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxscore = 0
        heap = []

        for num in nums:
            heap.append(-num)

        heapq.heapify(heap)

        while(k):   
            large = -heapq.heappop(heap)
            maxscore += large
            heapq.heappush(heap, -ceil(large / 3))
            k -= 1

        return maxscore