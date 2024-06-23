class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        flag = False

        for num in nums:
            if not flag:
                check = num 
            else:
                check = 1 - num

            if check == 0:
                count += 1
                flag = not flag

        return count