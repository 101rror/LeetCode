class Solution:
    def numSteps(self, s: str) -> int:
        dec = int(s, 2)
        count = 0

        while dec != 1:
            if dec % 2:
                dec += 1
            else:
                dec //= 2
            count += 1

        return count        