class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = x = 0

        for i in s:
            if i == 'L':
                x += 1
            if i == 'R':
                x -= 1
            if x == 0:
                count += 1

        return count