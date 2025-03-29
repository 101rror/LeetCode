class Solution:
    def reverseDegree(self, s: str) -> int:
        d = {x: i + 1 for i, x in enumerate("zyxwvutsrqponmlkjihgfedcba")}

        rvssum = 0
        for i in range(len(s)):
            rvssum += d[s[i]] * (i + 1)

        return rvssum
