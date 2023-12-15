class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = set()
        dct = set()

        for i in paths:
            src.add(i[0])
            dct.add(i[1])

        return list(dct - src)[0]