class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        idx = 0

        for i in range(n):
            if word[i] == ch:
                idx = i
                break

        if idx == 0:
            return word

        ans = word[:idx + 1][::-1] + word[idx + 1:]

        return ans
