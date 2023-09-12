class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            nums[i] = int(math.pow(nums[i], 2))
        
        nums = sorted(nums)
        return nums