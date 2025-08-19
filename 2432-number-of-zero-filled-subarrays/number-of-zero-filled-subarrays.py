class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        count, ans = 0, 0

        for i in range(n):
            if nums[i] == 0:
                count += 1
                ans += count
            else:
                count = 0

        return ans
