class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even = []
        odd = []

        for i in nums:
            if(i % 2):
                odd.append(i)
            else:
                even.append(i)

        even = sorted(even, reverse = True)

        for i in odd:
            even.append(i)
    
        return even