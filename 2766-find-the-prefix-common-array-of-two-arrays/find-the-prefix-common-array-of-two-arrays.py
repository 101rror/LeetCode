class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = []

        for i in range(n):
            AA = A[0 : i + 1]
            BB = B[0 : i + 1]
            st = list(set(AA) & set(BB))
            C.append(len(st))

        return C
