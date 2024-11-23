class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: list[int], previousCost: list[int]) -> int:
        ans = 0

        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            
            fdist = (ord(ct) - ord(cs)) % 26
            bdist = (ord(cs) - ord(ct)) % 26
            
            fcost = sum(nextCost[(ord(cs) - ord('a') + j) % 26] for j in range(fdist))
            bcost = sum(previousCost[(ord(cs) - ord('a') - j) % 26] for j in range(bdist))
            
            ans += min(fcost, bcost)

        return ans