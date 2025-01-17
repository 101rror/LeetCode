class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        dp = [0]

        for i in range(n):
            dp.append(derived[i] ^ dp[i])
        check0 = dp[0] == dp[-1]

        dp = [1]

        for i in range(n):
            dp.append(derived[i] ^ dp[i])
        check1 = dp[0] == dp[-1]

        return check0 or check1
