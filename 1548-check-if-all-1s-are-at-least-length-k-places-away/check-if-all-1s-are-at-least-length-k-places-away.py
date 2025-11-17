class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count, foundOne = 0, 0

        for i in range(1, n):
            if nums[i - 1] == nums[i] and nums[i - 1] == 1 and k > 0:
                return False

        for num in nums:
            if num == 1:
                foundOne = 1
            if foundOne and num == 0:
                count += 1
            else:
                if count != 0 and count < k:
                    return False
                else:
                    count = 0

        if nums[n - 1] != 0 and count != 0 and count < k:
            return False

        return True
