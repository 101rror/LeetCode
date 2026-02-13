class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        prefix = [[0, 0, 0]]

        for ch in s:
            prefix.append(prefix[-1][:])
            prefix[-1]["abc".index(ch)] += 1

        ans = 0
        freq = {}

        for i, (a, b, c) in enumerate(prefix):
            for k in [
                (-1, a - b, a - c),
                (-2, a - b, c),
                (-3, b - c, a),
                (-4, c - a, b),
                (-5, b, c),
                (-6, c, a),
                (-7, a, b),
            ]:
                if not k in freq:
                    freq[k] = i
                else:
                    ans = max(ans, i - freq[k])

        return ans
