class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(0, len(nums), 3):
            if(k < nums[i + 2] - nums[i]):
                return []
            ans.append(nums[i : i + 3])

        return ans