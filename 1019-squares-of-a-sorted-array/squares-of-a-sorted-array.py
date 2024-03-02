class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            x = (nums[i] ** 2)
            nums[i] = x

        nums.sort()
        
        return nums