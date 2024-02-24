class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                x = nums[i]
                nums[i] += (nums[i - 1] - nums[i]) + 1
                count += nums[i] - x
                
        return count