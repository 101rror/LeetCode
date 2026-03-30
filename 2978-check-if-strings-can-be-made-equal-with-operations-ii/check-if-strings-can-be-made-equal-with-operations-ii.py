class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        e1, o1, e2, o2 = [], [], [], []

        for i, (a, b) in enumerate(zip(s1, s2)):
            if i & 1:
                o1.append(a)
                o2.append(b)
            else:
                e1.append(a)
                e2.append(b)

        return sorted(e1) == sorted(e2) and sorted(o1) == sorted(o2)
