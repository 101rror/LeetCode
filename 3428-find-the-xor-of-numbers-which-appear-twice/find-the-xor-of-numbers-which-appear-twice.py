class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans, st = 0, set()
 
        for num in nums:
            if num in st:
                ans ^= num
            else:
                st.add(num)  

        return ans