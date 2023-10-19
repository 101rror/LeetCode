class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(S):
            ans = []
            
            for i in S:
                if(i != '#'):
                    ans.append(i)
                elif ans:
                    ans.pop()
            
            return ans

        if(check(s) == check(t)):
            return True
        else:
            return False
        