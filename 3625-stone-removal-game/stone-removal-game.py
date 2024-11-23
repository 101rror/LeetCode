class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice = True

        while n > 0:
            if n < remove:
                return not alice

            n -= remove
            remove -= 1

            if remove == 0:
                remove = 10
            
            alice = not alice

        return not alice