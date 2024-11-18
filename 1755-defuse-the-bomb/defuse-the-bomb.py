class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0 for i in code]

        ans = code
        code = code * 2

        for i in range(n):
            if k > 0:
                ans[i] = sum(code[i + 1 : i + k + 1])
            else:
                ans[i] = sum(code[i + n + k : i + n])

        return ans