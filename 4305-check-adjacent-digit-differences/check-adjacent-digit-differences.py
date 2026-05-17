class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        nums = list(s)

        for i in range(1, len(nums)):
            if abs(int(nums[i - 1]) - int(nums[i])) > 2:
                return False

        return True
