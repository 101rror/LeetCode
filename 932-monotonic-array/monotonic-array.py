class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nsorted = sorted(nums)
        rsorted = sorted(nums, reverse = True)

        if(nsorted == nums or rsorted == nums):
            return True

        return False