class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        ans = []

        for num in nums:
            mp[num] += 1

        for val in mp.values():
            ans.append(val)

        ans = sorted(ans, reverse=True)

        if ans[0] == 1:
            return sum(ans)
        else:
            mx = ans[0]
            tsum = 0
            for num in ans:
                if num == mx:
                    tsum += num

            return tsum
