class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def f(i, mod):
            if i < 0:
                return 0 if mod == 0 else -(1 << 30)
            x = nums[i]
            Pre = (mod - x) % 3

            if Pre < 0:
                Pre += 3

            return max(x + f(i - 1, Pre), f(i - 1, mod))

        return max(0, f(n - 1, 0))
