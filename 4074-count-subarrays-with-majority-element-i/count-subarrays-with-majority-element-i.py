class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for l in range(n):
            count = 0
            for r in range(l, n):
                if nums[r] == target:
                    count += 1

                ln = r - l + 1

                if count > ln // 2:
                    ans += 1

        return ans
