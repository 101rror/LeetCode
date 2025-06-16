class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxDif = 0
        minNum = nums[0]

        for i in range(n):
            dif = nums[i] - minNum
            maxDif = max(maxDif, dif)
            minNum = min(minNum, nums[i])

        return maxDif if maxDif > 0 else -1
