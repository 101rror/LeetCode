class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        score = 0

        while heap:
            num, idx = heapq.heappop(heap)
            if nums[idx] != -1:
                score += num
                nums[idx] = -1
                if idx > 0 and nums[idx - 1] != -1:
                    nums[idx - 1] = -1
                if idx < n - 1 and nums[idx + 1] != -1:
                    nums[idx + 1] = -1

        return score
