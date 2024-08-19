class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def check(sublist):
            for i in range(len(sublist) - 1):
                if sublist[i] + 1 != sublist[i + 1]:
                    return False

            return True


        n = len(nums)
        sublist = [nums[i : i + k] for i in range(n - k + 1)]
        ans = []

        for lst in sublist:
            if check(lst):
                mx = max(lst)
                ans.append(mx)

            else:
                ans.append(-1)

        return ans