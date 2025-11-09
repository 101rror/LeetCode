class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0

        while num1 and num2:
            if num1 > num2:
                num1 -= num2
            elif num1 < num2:
                num2 -= num1
            else:
                count += 1
                return count
            count += 1

        return count
