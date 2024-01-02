class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        st = set(nums)
        res = []
        mp = defaultdict(int)

        for i in nums:
            mp[i] += 1
         
        for i in st:
            x = nums.count(i)
            res.append(x)
        
        res.sort(reverse = True)
        t = res[0]

        ans = []

        for i in range(t):
            a = []
            for j, k in mp.items():
                if k != 0:
                    mp[j] -= 1
                    a.append(j)
            ans.append(a)

        return ans