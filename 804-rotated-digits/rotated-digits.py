class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0

        for i in range(1, n + 1):
            num = i
            flag = True
            check = False

            while num > 0:
                dig = num % 10

                if dig in [3, 4, 7]:
                    flag = False
                    break

                if dig in [2, 5, 6, 9]:
                    check = True

                num //= 10

            if flag and check:
                count += 1

        return count
