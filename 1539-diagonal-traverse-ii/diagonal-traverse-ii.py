class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n):
            x = len(nums[i])

            for j in range(x):
                ans.append([i + j, j, nums[i][j]])

        ans.sort()
        res = []
        for x, y, z in ans:
            res.append(z)
            
        return res
