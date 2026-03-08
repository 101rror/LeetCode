class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = ""

        for i in range(n):
            if nums[i][i] == "0":
                ans += "1"
            else:
                ans += "0"

        return ans
