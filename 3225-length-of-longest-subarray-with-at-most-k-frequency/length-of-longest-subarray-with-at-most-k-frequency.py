class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        ans = num = 0

        for i, x in enumerate(nums): 
            mp[x] += 1
            while mp[x] > k: 
                mp[nums[num]] -= 1
                num += 1
            ans = max(ans, i - num + 1)

        return ans 