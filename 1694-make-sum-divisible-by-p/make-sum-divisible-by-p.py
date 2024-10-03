class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        tsum = 0

        for num in nums:
            tsum = (tsum + num) % p

        mod = tsum % p

        if mod == 0:
            return 0

        mp = {0: -1}
        cur = 0
        mn = n

        for i in range(n):
            cur = (cur + nums[i]) % p

            need = (cur - mod + p) % p

            if need in mp:
                mn = min(mn, i - mp[need])

            mp[cur] = i

        if mn == n:
            return -1
        else:
            return mn 