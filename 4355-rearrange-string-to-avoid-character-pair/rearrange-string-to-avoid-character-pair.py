class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        xc = []
        yc = []
        ot = []

        for c in s:
            if c == y:
                yc.append(c)
            elif c == x:
                xc.append(c)
            else:
                ot.append(c)

        return "".join(yc + ot + xc)
