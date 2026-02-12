class Solution:
    def longestBalanced(self, s: str) -> int:
        def checkBalance(freq, tar):
            for ch in freq:
                if ch != 0 and ch != tar:
                    return False
            return True

        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord("a")] += 1
                if checkBalance(freq, freq[ord(s[j]) - ord("a")]):
                    ans = max(ans, j - i + 1)

        return ans
