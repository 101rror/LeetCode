class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def f(i, mod):
            if i < 0:
                return 0 if mod == 0 else -(1 << 30)
            x = nums[i]
            modPrev = (mod - x) % 3

            if modPrev < 0:
                modPrev += 3

            return max(x + f(i - 1, modPrev), f(i - 1, mod))

        return max(0, f(n - 1, 0))
