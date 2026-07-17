class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        first, second = 0, 0
        flag = True

        for i, n in enumerate(nums):
            if n % 2 == 1:
                flag = not flag
            if i % 6 == 5:
                flag = not flag

            if flag:
                first += n
            else:
                second += n

        return first - second
