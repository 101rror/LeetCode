class Solution:
    def kthCharacter(self, k: int) -> str:
        bn = bin(k - 1).count('1')

        return chr(ord('a') + bn)