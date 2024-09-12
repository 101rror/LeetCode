class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowedset = set(allowed)

        for i in words:
            if set(i).issubset(allowedset):
                count += 1

        return count