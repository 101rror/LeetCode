class Solution:
    def maxDepth(self, s):
        count = 0
        mx = 0

        for i in s:
            if i == "(":
                count += 1
                if mx < count:
                    mx = count
            if i == ")":
                count -= 1

        return(mx)