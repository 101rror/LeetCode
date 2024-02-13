class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(int)
        x = 0
        if n & 1:
            x = (n // 2) + 1
        else:
            x = (n // 2)

        nums.sort()
        ans = []
        
        for i in nums:
            mp[i] += 1

        for key, value in mp.items():
            if value >= x:
                return key

        return 0
