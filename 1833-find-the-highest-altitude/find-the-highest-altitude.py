class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre = 0
        ans = [0]

        for num in gain:
            pre += num
            ans.append(pre)

        return max(ans)
