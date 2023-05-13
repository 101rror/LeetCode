class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        m = len(nums[0])

        if ((n * m) != (r * c)):
            return nums

        else:
            lst = []
            ans = []

            for i in range(n):
                lst.extend(nums[i])

            for i in range(r):
                ans.append(lst[i*c:i*c+c])
            return ans