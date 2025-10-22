class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        freq = Counter(nums)
        ans = 1

        for v, t in freq.items():
            low = v - k
            high = v + k
            L = bisect.bisect_left(nums, low)
            R = bisect.bisect_right(nums, high)
            mid = R - L - t
            x = min(mid, numOperations)
            ans = max(ans, t + x)

        l = 0
        for r in range(n):
            while l <= r and nums[r] - nums[l] > 2 * k:
                l += 1
            ans = max(ans, min(r - l + 1, numOperations))

        return ans
