from collections import defaultdict


class Solution:
    def maxFrequency(self, nums, k, numOperations):
        mp = defaultdict(int)
        freq = defaultdict(int)

        minrange = int(1e9)
        maxrange = -int(1e9)

        for num in nums:
            freq[num] += 1
            l = num - k
            r = num + k

            minrange = min(minrange, l)
            maxrange = max(maxrange, r)
            mp[l] += 1
            mp[r + 1] -= 1

        ans = 1
        for i in range(minrange, maxrange + 1):
            mp[i] += mp[i - 1]
            cnt = freq[i]
            maxfreq = mp[i] - cnt
            maxfreq = min(maxfreq, numOperations)
            ans = max(ans, cnt + maxfreq)

        return ans
