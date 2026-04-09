from numpy import array


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        f = lambda x, y: (x * y) % mod
        nums = array(nums)
        tally = 1
        d = defaultdict(lambda: 1)

        for l, r, k, v in queries:
            r += 1
            if k > 1:
                nums[l:r:k] = f(nums[l:r:k], v)
            else:
                modInv = pow(v, mod - 2, mod)
                d[l], d[r] = f(d[l], v), f(d[r], modInv)

        for i, num in enumerate(nums):
            if i in d:
                tally = f(tally, d[i])
            if tally != 1:
                nums[i] = f(num, tally)

        return reduce(xor, map(int, nums))
