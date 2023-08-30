class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        n = len(encoded)

        for i in range(0, n + 1):
            if(i == 0):
                ans.append(0 ^ first)
            else:
                ans.append(encoded[i - 1] ^ ans[i - 1])
                
        return ans