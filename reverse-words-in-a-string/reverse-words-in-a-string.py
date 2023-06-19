class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ' '.join(s.split()[::-1])
        
        return ans