class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        prev, count = nums[0] - k, 1

        for i in range(1, n):
            minval = nums[i] - k
            maxval = nums[i] + k

            if prev < minval:
                prev = minval
            elif prev < maxval:
                prev += 1
            else:
                continue

            count += 1

        return count
