class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rvs = s[::-1]

        def sub(string):
            ans = []

            for i in range(len(string) - 1):
                ans.append(string[i : i + 2])

            return ans

        newstr = sub(s)
        revstr = sub(rvs)

        for i in newstr:
            if i in revstr:
                return True

        return False