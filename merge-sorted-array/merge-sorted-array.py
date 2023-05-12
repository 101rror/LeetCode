class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = nums1[:m]
        n1 = 0
        n2 = 0
        ans = []
        for i in range(n + m):
            if((n2 >= n) or (n1 < m and temp[n1] <= nums2[n2])):
                nums1[i] = temp[n1] 
                n1 += 1

            else:
                nums1[i] = nums2[n2]
                n2 += 1