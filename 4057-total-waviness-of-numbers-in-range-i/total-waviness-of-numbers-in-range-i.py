class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x: int) -> int:
            s = str(x)

            @cache
            def dp(pos, tight, started, prev1, prev2):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                ways = 0
                total = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, -1, -1)
                        ways += cnt
                        total += wav
                    else:
                        if not started:
                            cnt, wav = dp(pos + 1, ntight, True, d, -1)
                            ways += cnt
                            total += wav
                        else:
                            add = 0
                            if prev2 != -1:
                                if (prev2 < prev1 > d) or (prev2 > prev1 < d):
                                    add = 1

                            cnt, wav = dp(pos + 1, ntight, True, d, prev1)

                            ways += cnt
                            total += wav + add * cnt

                return ways, total

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)
