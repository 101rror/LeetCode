class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(num):
            x = str(num)
            n = len(x)
            count = 0

            for i in range(1, n - 1):
                if x[i - 1] < x[i] > x[i + 1] or x[i - 1] > x[i] < x[i + 1]:
                    count += 1

            return count

        count = 0
        for num in range(num1, num2 + 1):
            count += waviness(num)

        return count
