class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        newstr = ''

        for char in s:
            x = alpha.index(char) + 1
            newstr += str(x)

        new = int(newstr)
        ans = 0

        while(k):
            x = 0
            while(new):
                rem = new % 10
                x += rem
                new //= 10

            ans = x
            new = ans
            k -= 1

        return ans