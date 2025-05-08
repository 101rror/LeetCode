class Solution:
    def maxProduct(self, n: int) -> int:
        ans = []

        while n:
            rem = n % 10
            ans.append(rem)
            n //= 10

        ans.sort(reverse = True)

        return ans[0] * ans[1]