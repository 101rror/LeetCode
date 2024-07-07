class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = []
        n = len(s)
        
        for i in range(n):
            new = (i + k) % n
            ans.append(s[new])
        
        return ''.join(ans)
