class Solution:
    def maximumSwap(self, num: int) -> int:
        numstr = list(str(num))
        n = len(numstr)
        maxright = [0] * n

        maxright[n - 1] = n - 1

        for i in range(n - 2, -1, -1):
            if numstr[i] > numstr[maxright[i + 1]]:
                maxright[i] = i
            else:
                maxright[i] = maxright[i + 1]

        for i in range(n):
            if numstr[i] < numstr[maxright[i]]:
                numstr[i], numstr[maxright[i]] = numstr[maxright[i]], numstr[i]
                return int("".join(numstr))

        return num
