class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, sum(nums)
        count = 0

        for i in range(n):
            left += nums[i]
            right -= nums[i]

            if nums[i] != 0:
                continue
            if left == right:
                count += 2
            if abs(left - right) == 1:
                count += 1

        return count
