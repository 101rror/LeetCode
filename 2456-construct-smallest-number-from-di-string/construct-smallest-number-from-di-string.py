class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        nums = []
        countI = 0

        for i in range(1, n + 2):
            nums.append(str(i))

        for c in pattern:
            if c == "I":
                countI += 1

        if countI == n:
            new = nums[: countI + 1]
            return "".join(map(str, new))
        if countI == 0:
            nums.reverse()
            return "".join(nums)

        ans = []
        countD = 0

        for i in range(n):
            if pattern[i] == "I":
                for j in range(i, i - countD - 1, -1):
                    ans.append(str(j + 1))
                countD = 0
            else:
                countD += 1

        for i in range(n, n - countD - 1, -1):
            ans.append(str(i + 1))

        return "".join(ans)
