class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(x, s):
            rx = x[::-1]
            rs = s[::-1]
            ln = len(x)
            for i in range(ln):
                if x[i] != s[i]:
                    return False
            for i in range(ln):
                if rx[i] != rs[i]:
                    return False
            return True

        n = len(words)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if len(words[i]) <= len(words[j]):
                    if isPrefixAndSuffix(words[i], words[j]):
                        count += 1

        return count
