class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        maxwidth = 0
        maxarr = [0] * n

        maxarr[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            maxarr[i] = max(maxarr[i + 1], nums[i])   

        while right < n:
            while left < right and nums[left] > maxarr[right]:
                left += 1

            maxwidth = max(maxwidth, right - left)
            right += 1    

        return maxwidth