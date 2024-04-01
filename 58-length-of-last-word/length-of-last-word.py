class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = len(s.rstrip(' ').split(' ')[-1])

        return ans