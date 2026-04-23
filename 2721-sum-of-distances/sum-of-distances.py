class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        freq = {}

        for i, x in enumerate(nums):
            if x not in freq:
                freq[x] = []
            freq[x].append(i)

        ans = [0] * len(nums)

        for x, idxs in freq.items():
            tsum = sum(idxs)
            pre = 0
            m = len(idxs)

            for k, i in enumerate(idxs):
                diff = k - (m - k - 1) - 1
                ans[i] = diff * i - (2 * pre - tsum)
                pre += i

        return ans
