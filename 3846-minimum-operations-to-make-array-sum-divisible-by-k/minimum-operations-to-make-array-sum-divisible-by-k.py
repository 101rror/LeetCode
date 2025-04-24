class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)

        if total % k == 0:
            return 0

        return total % k
