class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        check = True

        for i in range(1, k):
            if nums[i] != nums[i - 1] + 1:
                check = False

        if check:
            ans.append(nums[k - 1])
        else:
            ans.append(-1)

        for i in range(k, n):
            if nums[i] != nums[i - 1] + 1:
                check = False

            if nums[i - k + 1] != nums[i - k] + 1:
                check = True
                for j in range(i - k + 2, i + 1):
                    if nums[j] != nums[j - 1] + 1:
                        check = False
                        break

            if check:
                ans.append(nums[i])
            else:
                ans.append(-1)

        return ans
