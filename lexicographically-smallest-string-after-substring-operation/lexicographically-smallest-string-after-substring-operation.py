class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)

        if s == "a" * n:
            return s[:-1] + "z"

        flag = False
        res = ""

        while s[0] == "a":
            res += "a"
            s = s[1:]

        for i in s:
            if i != "a":
                if not flag:
                    res += chr(ord(i) - 1)
                else:
                    res += i
            else:
                res += i
                flag = True

        return res