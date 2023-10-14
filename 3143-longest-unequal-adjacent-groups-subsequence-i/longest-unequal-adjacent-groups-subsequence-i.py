class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        ans = []
        ans.append(words[0])
        
        for i in range(0, n - 1):
            if(groups[i] != groups[i + 1]):
                ans.append(words[i + 1])
                
                
        return ans
        