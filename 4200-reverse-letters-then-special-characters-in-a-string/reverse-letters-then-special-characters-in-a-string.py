class Solution:
    def reverseByType(self, s: str) -> str:
        let = []
        spe = []

        for ch in s:
            if ch >= "a" and ch <= "z":
                let.append(ch)
            else:
                spe.append(ch)

        revLet = let[::-1]
        revSpe = spe[::-1]

        ans = ""
        li = si = 0

        for ch in s:
            if "a" <= ch <= "z":
                ans += revLet[li]
                li += 1
            else:
                ans += revSpe[si]
                si += 1

        return ans
