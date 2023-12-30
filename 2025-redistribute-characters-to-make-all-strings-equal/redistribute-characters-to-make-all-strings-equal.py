class Solution:
    def makeEqual(self, s: List[str]) -> bool:
        n = len(s)
        x = ''.join(s)
        st = set(x)
        mn = min(st)
        count = 0

        for i in st:
            if x.count(i) % n:
                return False

        return True