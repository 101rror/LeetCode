class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count = k - 1

        if count == 0:
            return True

        for i in range(k + 1, n):
            da = nums[i] - nums[i - 1]
            db = nums[i - k] - nums[i - k - 1]
            if da > 0 and db > 0:
                count -= 1
            else:
                count = k - 1

            if count == 0:
                return True

        return False
