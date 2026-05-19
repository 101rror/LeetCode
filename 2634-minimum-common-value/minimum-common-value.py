class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums = sorted(list(set(nums1) & set(nums2)))

        return nums[0] if nums else -1
