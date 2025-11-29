class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tsum = sum(nums)

        return tsum % k
