class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        even = sum(1 for x in nums if x % 2 == 0)
        odd = n - even

        for i in range(n):
            if nums[i] % 2 == 0:
                even -= 1
                ans[i] = odd
            else:
                odd -= 1
                ans[i] = even

        return ans
