class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        lst1 = set(nums1)
        lst2 = set(nums2)
        
        ans.append(sum(1 for num in nums1 if num in lst2))
        ans.append(sum(1 for num in nums2 if num in lst1))
        
        return ans