class Solution:
    def maxFreqSum(self, s: str) -> int:
        mpV = defaultdict(int)
        mpC = defaultdict(int)
        vowel = "aeiou"

        for ch in s:
            if ch in vowel:
                mpV[ch] += 1
            else:
                mpC[ch] += 1

        return max(mpV.values(), default=0) + max(mpC.values(), default=0)
