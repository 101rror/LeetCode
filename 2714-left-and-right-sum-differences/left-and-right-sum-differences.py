class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        vec1, vec2, ans = [], [], []

        sum1, sum2 = 0, 0

        vec1.append(0)

        for i in range(n - 1):
            sum1 += nums[i]
            vec1.append(sum1)

        nums.reverse()
        vec2.append(0)

        for i in range(n - 1):
            sum2 += nums[i]
            vec2.append(sum2)

        vec2.reverse()

        for i in range(n):
            ans.append(abs(vec1[i] - vec2[i]))

        return ans
