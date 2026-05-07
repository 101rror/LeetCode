class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref = [0] * n
        suff = [0] * n

        pref[0] = nums[0]

        for i in range(1, n):
            pref[i] = max(pref[i - 1], nums[i])

        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = min(suff[i + 1], nums[i])

        ans = pref[:]

        for i in range(n - 2, -1, -1):
            if pref[i] > suff[i + 1]:
                ans[i] = ans[i + 1]

        return ans
