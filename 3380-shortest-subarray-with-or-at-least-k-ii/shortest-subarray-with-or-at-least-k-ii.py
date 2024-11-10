class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bit = [-1 for _ in range(32)]
        j, cur, ans = 0, 0, float("inf")

        for i in range(n):
            cur |= nums[i]
            for b in range(32):
                if nums[i] & 1 << b: bit[b] = i

            while cur >= k and j <= i:
                ans = min(ans, i - j + 1)
                for b in range(32):
                    if nums[j] & 1 << b and bit[b] == j:
                        bit[b] = -1
                        cur ^= 1 << b
                j += 1 

        return ans if ans != float("inf") else -1