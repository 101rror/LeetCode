class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        ans = []

        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans