class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums and sum(nums) < target:
            return 0

        dic = {0: 1}

        for i in range(n):
            mp = defaultdict(int)
            for x in dic:
                mp[x + nums[i]] += dic[x]
                mp[x - nums[i]] += dic[x]
            dic = mp

        return dic[target]
