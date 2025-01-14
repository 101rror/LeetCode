class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seenA = set()
        seenB = set()
        common = set()
        C = []

        for i in range(n):
            seenA.add(A[i])
            seenB.add(B[i])

            if A[i] in seenB:
                common.add(A[i])
            if B[i] in seenA:
                common.add(B[i])
            C.append(len(common))

        return C