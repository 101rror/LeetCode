class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)
        ans = []

        for num in nums:
            mp[num] += 1

        for key, val in mp.items():
            if val == 2:
                ans.append(key)

        return ans
