class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        if n % 2 != 0:
            return False

        unlock = []
        openbr = []

        for i in range(n):
            if locked[i] == "0":
                unlock.append(i)
            elif s[i] == "(":
                openbr.append(i)
            elif s[i] == ")":
                if openbr:
                    openbr.pop()
                elif unlock:
                    unlock.pop()
                else:
                    return False

        while openbr and unlock and openbr[-1] < unlock[-1]:
            openbr.pop()
            unlock.pop()

        return False if openbr else True
