class Solution:
    def countCollisions(self, directions: str) -> int:
        left = right = ans = 0

        for ch in directions:
            if ch == "L":
                ans += left
            else:
                left = 1

        for ch in directions[::-1]:
            if ch == "R":
                ans += right
            else:
                right = 1

        return ans
