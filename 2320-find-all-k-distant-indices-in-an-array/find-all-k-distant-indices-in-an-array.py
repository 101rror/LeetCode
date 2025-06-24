class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    ans.append(i)
                    break

        return ans
