class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        first, last = 0, (n - 1)
        ans, mod = 0, 10**9 + 7

        while first <= last:
            if nums[first] + nums[last] > target:
                last -= 1

            else:
                ans += pow(2, last - first, mod)
                first += 1

        result = ans % mod

        return result
