class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = 0

        for i in t:
            count += ord(i)

        for i in s:
            count -= ord(i)

        ans = chr(count)
        
        return ans