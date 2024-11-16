class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = collections.Counter(nums[:k]) 
        tsum = sum(nums[:k])

        maxsum = 0
        if len(counter) == k:
            maxsum = tsum

        for i in range(k, n):
            x, y = nums[i], nums[i - k]
            tsum += x - y
            counter[x] += 1
            counter[y] -= 1

            if counter[y] == 0:
                del counter[y]
            if len(counter) == k:
                maxsum = max(maxsum, tsum)

        return maxsum