class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        x = 0

        if nums[0] < nums[n - 1]:
            x += 1

        for i in range(1, n):
            if (nums[i - 1] <= nums[i]) and x < 2:
                continue
            if nums[i - 1] > nums[i]:
                x += 1
            if x == 2:
                return False

        return True
