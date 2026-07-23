class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        mask = 0
        for num in nums:
            mask |= num

        return mask + 1
