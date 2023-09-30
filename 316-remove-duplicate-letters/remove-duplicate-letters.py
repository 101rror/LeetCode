class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        sets = {}

        for i in s:
            if(i in sets):
                sets[i] = sets[i] + 1
            else:
                sets[i] = 1
        ans = ""

        for i in s:
            if(i not in ans):
                while(len(ans) > 0 and ans[-1] > i and sets[ans[-1]] > 0):
                    ans = ans[:-1]
                ans = ans + i
                
            sets[i] = sets[i] - 1

        return ans