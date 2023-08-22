class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        x = columnNumber
        let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ""

        while(x >= 1):
            idx = (x - 1) % 26
            ans += chr(idx + 65) 
            x = (x - 1) // 26

        return ans[::-1]