class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mx, left = 0, 0

        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            mx = max(mx, right - left + 1)

        return n - mx
