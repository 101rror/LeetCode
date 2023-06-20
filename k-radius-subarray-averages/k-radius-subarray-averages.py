class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n, t = len(nums), 2*k
        ans = [-1] * n
        l, r = 0, t
        s = sum(nums[l:1+r])

        for i in range(k, n-k):
            ans[i] = s//(t+1)
            r += 1
            if r < n:s = s - nums[l] + nums[r]
            l += 1

        return ans

        