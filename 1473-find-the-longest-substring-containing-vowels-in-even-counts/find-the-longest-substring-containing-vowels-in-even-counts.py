class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        dic = {0: -1}
        mask, mx = 0, 0

        for i, x in enumerate(s):
            if x in vowel:
                mask ^= vowel[x]
            if mask in dic:
                mx = max(mx, i - dic[mask])
            else:
                dic[mask] = i

        return mx