class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = max(nums)
        seen = set(nums)
        slen = len(seen)
        count = nums.count(mx)

        if slen < n - 1 or mx == n or count != 2 or mx > n:
            return False
        else:
            return True
