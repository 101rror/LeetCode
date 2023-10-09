class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        no = [-1, -1]

        for i in range(n):
            if(nums[i] == target):
                ans.append(i)

        if(len(ans) == 0):
            return no
        else:
            return ans[0], ans[len(ans) - 1]