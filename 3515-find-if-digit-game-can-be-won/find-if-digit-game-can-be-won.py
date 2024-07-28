class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        ssum = 0
        dsum = 0

        for i in nums:
            if i < 10:
                ssum += i
            else:
                dsum += i

        return (False if ssum == dsum else True)