class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums[:] = nums[-k:] + nums[:-k]

        return nums
        