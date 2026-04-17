class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        freq = {}
        ans = float("inf")

        for k, v in enumerate(nums):
            if v in freq:
                ans = min(ans, k - freq[v])
            x, r = v, 0

            while x:
                r = r * 10 + x % 10
                x //= 10

            freq[r] = k

        return -1 if ans == float("inf") else ans
