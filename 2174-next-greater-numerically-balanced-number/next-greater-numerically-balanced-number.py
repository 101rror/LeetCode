class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        x = n + 1

        while True:
            s = str(x)
            if "0" not in s:
                c = Counter(s)
                flag = True

                for d in c:
                    if c[d] != int(d):
                        flag = False
                        break

                if flag:
                    return x

            x += 1
