class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        tsum = 0
        qt = 1

        for i in range(len(nums)):
            tsum += qt * (nums[i] + nums[-i - 1])
            qt = 2 * qt - comb(i, k - 1)

        return tsum % mod