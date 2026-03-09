class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        @cache
        def build(a: int, b: int, prev: int) -> int:
            if a == 0 and b == 0:
                return 1

            ans = 0

            for i in range(1, limit + 1):
                if i <= a and prev != 0:
                    ans += build(a - i, b, 0)
                if i <= b and prev != 1:
                    ans += build(a, b - i, 1)

            return ans

        return build(zero, one, 2) % (10**9 + 7)
