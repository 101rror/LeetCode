class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        ans = []
        mn = float("inf")

        for i in range(1, n):
            x = abs(arr[i] - arr[i - 1])
            if x < mn:
                mn = x
                ans = [[arr[i - 1], arr[i]]]
            elif x == mn:
                ans.append([arr[i - 1], arr[i]])

        return ans
