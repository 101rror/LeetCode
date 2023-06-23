class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        hm = [defaultdict() for i in range(len(nums))]
        ans = 0
        maxi =- 1

        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                diff = nums[i]-nums[j]
                if diff not in hm[j]:
                    hm[j][diff] = 1
                if diff not in hm[i]:
                    hm[i][diff] = hm[j].get(diff,1)+1
                else:
                    hm[i][diff] = max(hm[j][diff]+1, hm[i][diff])

                ans = max(ans, hm[i][diff])
        
        return ans
