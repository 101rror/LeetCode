class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans = []
        nums = []
        cnt = 0
        
        for word in words:
            if word == "prev":
                if(cnt < len(nums)):
                    ans.append(nums[len(nums) - 1 - cnt])
                else:
                    ans.append(-1)
                    
                cnt += 1
                    
            else:
                nums.append(int(word))
                cnt = 0
        
        return ans