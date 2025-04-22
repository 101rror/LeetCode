class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xd = abs(x - z)
        yd = abs(y - z)

        if xd < yd:
            return 1
        elif xd > yd:
            return 2
        else:
            return 0
