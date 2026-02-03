class Solution:
    def isTrionic(self, nums: List[int], k: int = 3) -> bool:
        n = len(nums)
        sg, sw = 1, 0

        for i in range(1, n):
            dif = nums[i] - nums[i - 1]
            if dif == 0:
                return False
            elif dif * sg < 0:
                sg *= -1
                sw += 1

        return sw == k - 1 if nums[0] < nums[1] else False
