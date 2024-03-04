class Solution:
    def bagOfTokensScore(self, token: List[int], power: int) -> int:
        n = len(token)
        token.sort()
        first, last, count, mx = 0, n - 1, 0, 0

        if n == 0:
            return 0
        if n == 1:
            if token[0] <= power:
                return 1
            else:
                return 0
        
        while(first <= last):
            if token[first] <= power:
                count += 1
                power -= token[first]
                first += 1
                mx = max(mx, count)
            elif count > 0:
                count -= 1
                power += token[last]
                last -= 1
            else:
                return mx

        return mx