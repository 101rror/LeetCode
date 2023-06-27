class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        ln1 = len(nums1)
        ln2 = len(nums2)

        for i in range(min(ln1, k)):
            heappush(ans, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
    
        res = []
        while (ans and len(res) < k):
            _, n1, n2, j = heappop(ans)
            print(_)
            res.append([n1, n2])

            if (j + 1 < ln2):
               heappush(ans, (n1 + nums2[j + 1], n1, nums2[j + 1], j + 1))

        return res
   

        