class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                count += 1

        if count > 1 or (count == 1 and nums[0] < nums[n - 1]):
            return False

        return True
