import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        heap = []

        for i in range(n):
            initial = 0
            for j in range(i, n):
                initial += nums[j]
                heapq.heappush(heap, initial)

        ans = 0

        for i in range(1, right + 1):
            x = heapq.heappop(heap)
            if i >= left:
                ans += + x

        return ans % mod