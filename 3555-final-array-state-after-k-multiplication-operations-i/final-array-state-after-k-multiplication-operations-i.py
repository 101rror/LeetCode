class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while(k):
            x = min(nums)
            t = 0

            for i in range(len(nums)):
                if nums[i] == x and t == 0:
                    nums[i] = x * multiplier
                    t = 1

            k -= 1

        return nums