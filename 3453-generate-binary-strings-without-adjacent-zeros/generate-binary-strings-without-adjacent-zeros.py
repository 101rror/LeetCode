class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def dfs(s):
            if len(s) == n:
                ans.append(s)
            else:
                if not s or s[-1] == "1":
                    dfs(s + "0")
                dfs(s + "1")

        dfs("")
        return ans
