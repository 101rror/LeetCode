class Solution:
    def guessNumber(self, n: int) -> int:
        first = 0
        last = n - 1

        while(first <= last):
            mid = (first + last) // 2
            ans = guess(mid)

            if(ans == 0):
                return mid
            elif(ans < 0):
                last = (mid - 1)
            else:
                first = (mid + 1)

        return first