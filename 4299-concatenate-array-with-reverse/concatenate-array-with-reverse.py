class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = []

        for num in nums:
            ans.append(num)

        nums.reverse()

        for num in nums:
            ans.append(num)

        return ans
