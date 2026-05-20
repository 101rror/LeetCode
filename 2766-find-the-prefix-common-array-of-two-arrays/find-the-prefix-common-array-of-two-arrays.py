class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []

        for i in range(1, n + 1):
            nums1 = A[0:i]
            nums2 = B[0:i]
            nums = list(set(nums1) & set(nums2))
            ans.append(len(nums))

        return ans
