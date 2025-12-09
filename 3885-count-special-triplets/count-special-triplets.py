class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        ans, n = 0, len(nums)
        left = Counter()
        right = Counter(nums)

        for i in range(n):
            right[nums[i]] -= 1

            tar = nums[i] * 2
            ans += (left[tar] * right[tar]) % mod

            left[nums[i]] += 1

        return ans % mod
