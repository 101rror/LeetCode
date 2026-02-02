class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        srt = SortedList(nums[1 : 1 + dist])
        cSum, mSum = sum(srt[: k - 2]), float("inf")

        for i in range(1 + dist, n):
            if srt.bisect(nums[i]) <= k - 2:
                cSum += nums[i]
            else:
                cSum += srt[k - 2]

            mSum = min(mSum, cSum)
            srt.add(nums[i])

            if srt.bisect(nums[i - dist]) <= k - 2:
                cSum -= nums[i - dist]
            else:
                cSum -= srt[k - 2]
            srt.remove(nums[i - dist])

        return nums[0] + mSum
