class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        lst1 = list(set(nums1))
        lst2 = list(set(nums2))
        mp = defaultdict(int)

        for i in lst1:
            mp[i] += 1
        for i in lst2:
            mp[i] += 1

        for i, j in mp.items():
            if j == 2:
                ans.append(i)

        return ans