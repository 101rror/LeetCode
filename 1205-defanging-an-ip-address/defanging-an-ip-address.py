class Solution:
    def defangIPaddr(self, address: str) -> str:
        x = address.split('.')
        ans = '[.]'.join(x)

        return ans