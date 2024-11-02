class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = list(sentence.split())

        if len(lst) == 1:
            return sentence[0] == sentence[len(sentence) - 1]

        if sentence[0] == sentence[len(sentence) - 1]:
            ans = []

            for i in range(len(lst)):
                s = lst[i]
                ans.append(s[0])
                if len(s) > 1:
                    ans.append(s[len(s) - 1])

            for i in range(1, len(ans) - 1):
                if ans[i - 1] != ans[i] != ans[i + 1]:
                    return False

            return True

        return False