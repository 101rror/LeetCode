class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        cur = 1

        for i in range(n):
            ans.append(cur)

            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10

        return ans
