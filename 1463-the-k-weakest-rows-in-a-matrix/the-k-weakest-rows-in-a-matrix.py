class Solution:
    def kWeakestRows(self, G: List[List[int]], k: int) -> List[int]:
        S = [[sum(g),i] for i,g in enumerate(G)]
        R = sorted(S)
        return [r[1] for r in R[:k]]