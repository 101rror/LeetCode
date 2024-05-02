class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        num = nums
        i = 0

        for i in range(len(nums)):
            if nums[i] < 0 and abs(nums[i]) in num:
                return abs(nums[i])

            i += 1

        return -1
