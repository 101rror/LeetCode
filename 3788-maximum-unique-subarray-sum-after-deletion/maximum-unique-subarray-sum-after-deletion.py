class Solution:
    def maxSum(self, nums: List[int]) -> int:
        st = set()
        maxsum = 0

        for num in nums:
            if num not in st and num > 0:
                maxsum += num
            st.add(num)

        return maxsum if maxsum > 0 else max(nums)
