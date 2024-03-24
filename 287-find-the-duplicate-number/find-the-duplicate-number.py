class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        st = set()

        for num in nums:
            if num in st:
                return num
            st.add(num)