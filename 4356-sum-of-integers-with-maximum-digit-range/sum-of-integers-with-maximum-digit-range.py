class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        MAX = float("-inf")
        ans = 0

        for num in nums:
            mx, mn = 0, 9
            x = num

            while x > 0:
                r = x % 10
                mn = min(mn, r)
                mx = max(mx, r)
                x //= 10

            dr = mx - mn

            if dr > MAX:
                MAX = dr
                ans = num
            elif dr == MAX:
                ans += num

        return ans
