class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)

        if ones == 0:
            return 0

        nums += nums
        mx = curr = sum(nums[:ones])
        n = len(nums) // 2

        for i in range(1, n):
            curr = curr - nums[i - 1] + nums[i + ones - 1]
            mx = max(mx, curr)

        return ones - mx