class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1
        flag = False

        for num in arr:
            if flag and num >= ans + 1:
                ans += 1
            else:
                flag = True

        return ans
