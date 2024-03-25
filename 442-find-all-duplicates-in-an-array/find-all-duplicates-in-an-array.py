class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        st = Counter(nums)
        ans = []

        for i, j in st.items():
            if j >= 2:
                ans.append(i)

        return ans
