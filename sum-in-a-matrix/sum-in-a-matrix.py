class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        mxsum = 0
        nums = [sorted(i) for i in nums]

        while any(nums):
            temp = 0
            for i in nums:
                temp = max(temp, i.pop())
            mxsum += temp

        return mxsum
        