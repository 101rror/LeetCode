class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(1 << n):
            XOR = 0
            for j in range(n):
                if i & 1:
                    XOR ^= nums[j]
                i >>= 1
                
            ans += XOR

        return ans