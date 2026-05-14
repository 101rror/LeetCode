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
            new = list(seen)
            for i in range(1, slen):
                x = new[i] - new[i - 1]
                if x != 1:
                    return False

            return True
