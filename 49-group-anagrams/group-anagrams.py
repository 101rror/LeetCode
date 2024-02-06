class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            srt = ''.join(sorted(s))

            if(srt not in ans):
                ans[srt] = []

            ans[srt].append(s)

        return list(ans.values())