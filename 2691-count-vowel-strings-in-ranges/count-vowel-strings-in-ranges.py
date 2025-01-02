class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowel = "aeiou"

        dp = [1 if word[0] in vowel and word[-1] in vowel else 0 for word in words]

        prefixsum = [0] * (n + 1)
        for i in range(n):
            prefixsum[i + 1] = prefixsum[i] + dp[i]

        ans = []

        for start, end in queries:
            count = prefixsum[end + 1] - prefixsum[start]
            ans.append(count)

        return ans
