class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0

        for ch in patterns:
            if ch in word:
                count += 1

        return count
