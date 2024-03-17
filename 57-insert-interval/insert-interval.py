class Solution:
    def insert(self, inv: List[List[int]], nw: List[int]) -> List[List[int]]:
        test = True
        n = len(inv)

        for i in range(n):
            if inv[i][0] > nw[0]:
                test = False
                inv.insert(i, nw)
        if test:
            inv.append(nw)

        i = 1

        while i < len(inv):
            if inv[i - 1][1] >= inv[i][0]:
                inv[i - 1][1] = max(inv[i - 1][1], inv[i][1])
                inv.pop(i)
            else:
                i += 1
            
        return inv