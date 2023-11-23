class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(num: List[int]):
            num.sort()
            x = num[1] - num[0]

            for i in range(1, len(num)):
                if(num[i] - num[i - 1] != x):
                    return False

            return True

        ans = []
        n = len(nums)
        n1 = len(l)
        res = []

        for i in range(n1):
            le = l[i]
            ri = r[i]

            for i in range(le, ri + 1):
                res.append(nums[i])
            
            if(check(res)):
                ans.append(True)
            else:
                ans.append(False)
                
            res.clear()

        return ans