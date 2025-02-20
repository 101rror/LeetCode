class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""

        for i in range(len(nums)):
            if nums[i][i] == "0":
                ans += "1"
            else:
                ans += "0"

        return ans
