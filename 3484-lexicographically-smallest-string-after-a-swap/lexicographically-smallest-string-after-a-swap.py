class Solution:
    def getSmallestString(self, s: str) -> str:
        ans = [i for i in s]
        n = len(ans)

        for i in range(n - 1):
            x = int(ans[i])
            y = int(ans[i + 1])

            if x & 1 == y & 1 and x > y:
                ans[i + 1] = str(x)
                ans[i] = str(y)
                break

        return "".join(ans)