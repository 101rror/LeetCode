class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1, s2, s3 = str(num1).zfill(4), str(num2).zfill(4), str(num3).zfill(4)
        ans = ''

        for i in range(4):
            x, y, z = s1[i], s2[i], s3[i]

            ans += min(x, min(y, z))

        return int(ans)