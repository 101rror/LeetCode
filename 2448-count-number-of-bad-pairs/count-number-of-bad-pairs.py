class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        mp = dict()

        for i in range(n):
            nums[i] -= i
            if nums[i] not in mp:
                mp[nums[i]] = 0
            mp[nums[i]] += 1

        count = 0
        for key in mp:
            count += math.comb(mp[key], 2)

        return math.comb(n, 2) - count
