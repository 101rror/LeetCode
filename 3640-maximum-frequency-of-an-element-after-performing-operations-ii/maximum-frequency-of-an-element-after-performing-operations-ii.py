class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)

        if not nums:
            return 0

        freq = Counter(nums)
        ans = 1

        for v, t in freq.items():
            low = v - k
            high = v + k
            L = bisect.bisect_left(nums, low)
            R = bisect.bisect_right(nums, high)
            mid = R - L
            need = mid - t
            x = min(need, numOperations)
            ans = max(ans, t + x)

        l = 0
        for r in range(n):
            while l <= r and nums[r] - nums[l] > 2 * k:
                l += 1
            w = r - l + 1
            ans = max(ans, min(w, numOperations))

        return ans
