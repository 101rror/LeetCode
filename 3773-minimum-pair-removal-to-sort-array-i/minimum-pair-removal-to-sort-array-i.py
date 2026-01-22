class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count, mn, idx = 0, float('inf'), 0

        while nums != sorted(nums):
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < mn:
                    mn = nums[i] + nums[i + 1]
                    idx = i
            nums.pop(idx)
            nums[idx] = mn
            mn, idx = float('inf'), 0
            count += 1

        return count
