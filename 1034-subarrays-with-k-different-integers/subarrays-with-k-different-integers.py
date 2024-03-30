class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count1, count2 = 0, 0
        left, right = 0, 0
        freq1, freq2 = defaultdict(int), defaultdict(int)

        ans = 0

        for i in range(len(nums)):
            if freq1[nums[i]] == 0:
                count1 += 1
            freq1[nums[i]] += 1

            if freq2[nums[i]] == 0:
                count2 += 1
            freq2[nums[i]] += 1
            
            while count1 > k:
                freq1[nums[right]] -= 1
                if freq1[nums[right]] == 0:
                    count1 -= 1
                right += 1
            
            while count2 > k - 1:
                freq2[nums[left]] -= 1
                if freq2[nums[left]] == 0:
                    count2 -= 1
                left += 1
            
            ans += left - right
        
        return ans