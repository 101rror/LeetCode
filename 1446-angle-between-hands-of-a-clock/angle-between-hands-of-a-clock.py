class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = 6.0 * minutes
        h = 30.0 * (hour % 12) + 0.5 * minutes

        d = abs(h - m)

        return min(d, 360.0 - d)
