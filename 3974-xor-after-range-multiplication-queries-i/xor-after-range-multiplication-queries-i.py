class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 1000000007
        ans = 0

        for t in queries:
            l = t[0]
            r = t[1]
            k = t[2]
            v = t[3]

            idx = l

            while idx <= r:
                temp = nums[idx]
                nums[idx] = (temp * v) % mod
                idx += k

        for num in nums:
            ans ^= num

        return ans
