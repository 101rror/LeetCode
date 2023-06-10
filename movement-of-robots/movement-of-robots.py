class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(s)

        for i in range(n):
            if (s[i] == 'L'):
                nums[i] -= d
            else:
                nums[i] += d
                
        Tsum = 0
        nums = sorted(nums)

        mod = 10 ** 9 + 7
        res = 0
        
        for i in range(n):
            Tsum += (nums[i] * i - res)
            Tsum %= mod
            res += nums[i]
            res %= mod
            
        ans = (Tsum % mod)

        return ans