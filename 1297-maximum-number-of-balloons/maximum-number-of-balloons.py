class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        ans = []

        for k, v in cnt.items():
            if k == "b" or k == "a" or k == "n":
                ans.append(v)
            if k == "l" or k == "o":
                ans.append(v // 2)

        return min(ans) if len(ans) == 5 else 0
