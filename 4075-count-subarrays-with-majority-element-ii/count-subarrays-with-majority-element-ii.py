class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = [0] * (2 * n + 1)
        cnt = n
        pref[cnt] = 1
        ans = presum = 0

        for x in nums:
            step = 1 if x == target else -1
            presum += pref[cnt] if step == 1 else -pref[cnt - 1]
            cnt += step
            pref[cnt] += 1
            ans += presum

        return ans
