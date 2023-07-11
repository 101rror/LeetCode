class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x, y = set(nums1), set(nums2)
        ans = []

        ans.append(list(x - y))
        ans.append(list(y - x))

        return ans
        