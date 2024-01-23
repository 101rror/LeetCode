class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = [""]
        mx = 0

        for i in arr:
            for j in ans:
                x = j + i
                if len(x) != len(set(x)):
                    continue
                else:
                    ans.append(x)
                
                mx = max(mx, len(x))

        return mx