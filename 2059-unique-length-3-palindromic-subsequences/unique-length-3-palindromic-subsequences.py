class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0

        for i in range(26):
            left, right = s.find(chr(i + 97)), s.rfind(chr(i + 97))
            if left != -1 and right != -1:
                count += len(set(s[left + 1 : right]))

        return count
