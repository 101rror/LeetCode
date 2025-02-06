from collections import Counter


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        counter = Counter()

        for i in range(n):
            for j in range(i):
                prod = nums[i] * nums[j]
                ans += counter[prod] * 8
                counter[prod] += 1

        return ans
