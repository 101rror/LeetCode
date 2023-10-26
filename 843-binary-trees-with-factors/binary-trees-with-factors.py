class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        ans = [1] * n
        MOD = 10**9 + 7
        arr.sort()

        for i in range(1, n):
            for j in range(0, i):
                if arr[i] % arr[j] == 0 :
                    if arr[i] // arr[j] in arr:
                        r = arr.index(arr[i] // arr[j])
                        ans[i] = ans[i] + ans[j] * ans[r]

        return sum(ans) % MOD
                    


        