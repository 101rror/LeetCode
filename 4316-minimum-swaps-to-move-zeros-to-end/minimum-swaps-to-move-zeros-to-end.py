class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        zero = nums.count(0)
        swap = 0

        for i in range(n - zero):
            if nums[i] == 0:
                swap += 1

        return swap
