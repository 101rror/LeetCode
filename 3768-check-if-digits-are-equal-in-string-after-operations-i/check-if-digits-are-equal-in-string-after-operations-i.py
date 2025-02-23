class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = []
        arr.append(s)

        while len(arr[-1]) != 2:
            res = ""
            for i in range(len(arr[-1]) - 1):
                res += str((int(arr[-1][i]) + int(arr[-1][i + 1])) % 10)
            arr.append(res)

        return arr[-1][0] == arr[-1][1]
