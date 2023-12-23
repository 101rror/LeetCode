class Solution:
    def isPathCrossing(self, path: str) -> bool:
        lst = [(0,0)]
        ew, ns = 0, 0

        for i in path:
            if i == 'N':
                ns += 1
            if i == 'S':
                ns -= 1
            if i == 'E':
                ew += 1
            if i == 'W':
                ew -= 1

            if (ew, ns) in lst:
                return True
            else:
                lst.append((ew, ns))

        return False