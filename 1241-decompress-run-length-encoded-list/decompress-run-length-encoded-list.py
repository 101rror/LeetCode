class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(0, n, 2):
            x = nums[i]
            y = nums[i + 1]

            for j in range(x):
                ans.append(y)

        return ans

        