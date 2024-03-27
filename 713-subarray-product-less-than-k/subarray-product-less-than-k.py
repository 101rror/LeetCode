class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0

        if k <= 1:
            return count

        left = 0
        mul = 1

        for right in range(len(nums)):
            mul *= nums[right]
            while mul >= k:
                mul /= nums[left]
                left += 1

            count += right - left + 1

        return count