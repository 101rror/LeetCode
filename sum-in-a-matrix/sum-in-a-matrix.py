class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = [sorted(row) for row in nums]
        ans = sum(max(row[i] for row in rows) for i in range(len(rows[0])))
        
        return ans