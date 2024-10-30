class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        maxmount = 0
        increase = [1] * n
        decrease = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    increase[i] = max(increase[i], increase[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    decrease[i] = max(decrease[i], decrease[j] + 1)

        for i in range(n):
            if increase[i] > 1 and decrease[i] > 1:
                maxmount = max(maxmount, increase[i] + decrease[i] - 1)

        return n - maxmount
