class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans=[]

        first = 0
        last = 0

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
          
        while (first < n1 and last < n2):
            
            if nums1[first] < nums2[last]:
                first += 1

            elif nums2[last] < nums1[first]:
                last += 1

            else:
                ans.append(nums1[first])
                first += 1
                last += 1
                
        return ans