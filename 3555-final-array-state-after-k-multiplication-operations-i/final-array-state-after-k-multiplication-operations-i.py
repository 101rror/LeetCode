class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        heap = []
        ans = [0] * n

        for idx, num in enumerate(nums):
            heap.append((num, idx))

        heapify(heap)

        while k:
            num, idx = heappop(heap)
            num *= multiplier
            heappush(heap, (num, idx))
            k -= 1

        while heap:
            num, idx = heappop(heap)
            ans[idx] = num

        return ans
