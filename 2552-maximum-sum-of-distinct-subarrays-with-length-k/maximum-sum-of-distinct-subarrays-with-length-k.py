class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter(nums[:k])
        ksum = sum(nums[:k])
        maxsum = 0

        if len(counter) == k:
            maxsum = ksum

        for i in range(k, n):
            fi, la = nums[i], nums[i - k]
            ksum += fi - la
            counter[fi] += 1
            counter[la] -= 1
            
            if counter[la] == 0:
                del counter[la]
            if len(counter) == k:
                maxsum = max(maxsum, ksum)

        return maxsum