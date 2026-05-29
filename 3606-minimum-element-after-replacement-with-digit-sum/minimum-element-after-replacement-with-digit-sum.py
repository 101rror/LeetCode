class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(num))) for num in nums)
