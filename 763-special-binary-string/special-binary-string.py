class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if s == "":
            return ""

        ans = []
        count = i = j = 0

        while i < len(s):
            if s[i] == "1":
                count += 1
            else:
                count -= 1
                
            if count == 0:
                ans.append("1" + self.makeLargestSpecial(s[j + 1 : i]) + "0")
                j = i + 1
            i += 1

        ans.sort(reverse=True)

        return "".join(ans)
