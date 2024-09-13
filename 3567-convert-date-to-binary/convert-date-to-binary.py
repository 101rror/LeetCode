class Solution:
    def convertDateToBinary(self, date: str) -> str:
        splitday = date.split('-')
        ans = ''

        for day in splitday:
            bn = bin(int(day))[2:]
            ans += bn
            ans += '-'

        return ans[:-1]