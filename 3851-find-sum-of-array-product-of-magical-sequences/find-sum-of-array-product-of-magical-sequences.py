MOD = 10**9 + 7
MAX = 55

fact = [1] * MAX
ifact = [1] * MAX
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD
    ifact[i] = pow(fact[i], -1, MOD)

from functools import cache

class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(idx: int, m_rem: int, k_rem: int, carry: int) -> int:
            if idx == n:
                if m_rem != 0:
                    return 0
                return 1 if k_rem == carry.bit_count() else 0

            res = 0
            for take in range(m_rem + 1):
                bit = (take + carry) % 2
                if k_rem >= bit:
                    res = (res + dp(idx + 1, m_rem - take, k_rem - bit, (carry + take) // 2)
                           * pow(nums[idx], take, MOD)
                           * ifact[take])
            return res

        ans = dp(0, M, K, 0)
        dp.cache_clear()
        return ans * fact[M] % MOD
