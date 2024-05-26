class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0

        for i in nums2:
            for j in nums1:
                if j % (i * k) == 0:
                    count += 1

        return count