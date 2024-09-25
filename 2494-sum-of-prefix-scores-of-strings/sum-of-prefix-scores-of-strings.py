class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n, dp, ans = len(words), {}, []

        for word in words:
            char = ''
            for ch in word:
                char += ch
                dp[char] = dp.get(char, 0) + 1

        for word in words:
            char = ''
            count = 0
            for ch in word:
                char += ch
                if char in dp:
                    count += dp[char]

            ans.append(count)

        return ans