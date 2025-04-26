class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0

        mn = mx = bound = -1

        for i in range(n):
            if nums[i] == minK:
                mn = i
            if nums[i] == maxK:
                mx = i
            if not minK <= nums[i] <= maxK:
                bound = i

            count += max(0, min(mn, mx) - bound)

        return count
