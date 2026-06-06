class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        ans = []

        for x in nums:
            total -= x
            ans.append(abs(left - total))
            left += x

        return ans
