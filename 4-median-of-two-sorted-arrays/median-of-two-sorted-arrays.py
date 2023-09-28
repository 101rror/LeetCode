import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mrg = nums1 + nums2
        mrg = sorted(mrg)

        ans = statistics.median(mrg)

        return ans
        