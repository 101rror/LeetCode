class Solution:
    def maxEqualRowsAfterFlips(self, mat: List[List[int]]) -> int:
        counter = Counter()
        
        for r in mat:
            pattern = tuple(r) if r[0] == 0 else tuple(bit ^ 1 for bit in r)
            counter[pattern] += 1
            
        return max(counter.values())