class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []

        for i in words:
            i = i.split(separator)

            for j in i:
                if j:
                    ans.append(j)

        return ans