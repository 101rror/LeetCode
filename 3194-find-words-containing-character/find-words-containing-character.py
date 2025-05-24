class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []

        for i in range(len(words)):
            s = words[i]

            for j in range(len(s)):
                if s[j] == x:
                    ans.append(i)
                    break

        return ans
