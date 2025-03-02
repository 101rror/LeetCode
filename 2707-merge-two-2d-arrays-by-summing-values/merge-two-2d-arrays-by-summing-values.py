class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        dct = {}

        for i in nums1:
            dct[i[0]] = i[1]

        for i in nums2:
            if i[0] not in dct.keys():
                dct[i[0]] = i[1]
            else:
                dct[i[0]] = i[1] + dct[i[0]]

        ans = []

        for i in sorted(dct.keys()):
            ans.append([i, dct[i]])

        return ans
