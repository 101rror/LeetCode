class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = 0

        for i in range(n):
            mx = max(mx, nums[i])
            nums[i] = gcd(mx, nums[i])

        nums.sort()

        left, right = 0, n - 1
        ans = 0

        while left < right:
            ans += gcd(nums[left], nums[right])
            left += 1
            right -= 1

        return ans
