class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        newbannedWords = set(bannedWords)

        for word in message:
            if word in newbannedWords:
                count += 1

        return True if count >= 2 else False
