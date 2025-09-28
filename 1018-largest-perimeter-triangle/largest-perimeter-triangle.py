class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=1)
        ans = 0

        for i in range(n - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                ans = max(ans, nums[i] + nums[i + 1] + nums[i + 2])

        return ans
