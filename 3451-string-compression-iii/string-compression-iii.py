class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        count = 1

        if len(word) == 1:
            ans += str(count)
            ans += word

        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                count += 1
            else:
                if count <= 9:
                    ans += str(count)
                    ans += word[i - 1]
                    count = 1
                else:
                    while count:
                        if count >= 9:
                            ans += str(9)
                            ans += word[i - 1]
                            count -= 9
                        else:
                            ans += str(count)
                            ans += word[i - 1]
                            count -= count

                    count = 1

            if i == len(word) - 1:
                if count > 9:
                    while count:
                        if count >= 9:
                            ans += str(9)
                            ans += word[i]
                            count -= 9
                        else:
                            ans += str(count)
                            ans += word[i]
                            count -= count
                else:
                    ans += str(count)
                    ans += word[i]

        return ans
