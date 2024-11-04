class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return "1" + word

        ans = []
        count = 1

        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                count += 1
            else:
                while count > 9:
                    ans.append("9" + word[i - 1])
                    count -= 9
                ans.append(str(count) + word[i - 1])
                count = 1

            if i == len(word) - 1:
                while count > 9:
                    ans.append("9" + word[i])
                    count -= 9
                ans.append(str(count) + word[i])

        return "".join(ans)
