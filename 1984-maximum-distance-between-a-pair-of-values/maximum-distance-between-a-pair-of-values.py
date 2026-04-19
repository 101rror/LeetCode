class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        l1 = len(nums1)
        l2 = len(nums2)

        for i in range(l1):
            first = i
            last = l2 - 1

            while first <= last:
                mid = (first + last) // 2
                if nums2[mid] >= nums1[i]:
                    first = mid + 1
                else:
                    last = mid - 1

            ans = max(ans, last - i)
            
        return ans
