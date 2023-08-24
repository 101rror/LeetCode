class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            ans.insert(index[i], nums[i])

        return ans