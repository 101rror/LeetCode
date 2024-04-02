class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sindex = []
        tindex = []

        for i in s:
            sindex.append(s.index(i))
        for i in t:
            tindex.append(t.index(i))

        if sindex == tindex:
            return True

        return False