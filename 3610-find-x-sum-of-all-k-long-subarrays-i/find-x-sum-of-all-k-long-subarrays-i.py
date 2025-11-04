class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i : i + k]
            freq = Counter(sub)

            most = nlargest(x, freq.items(), key=lambda item: (item[1], item[0]))
            checksum = sum(val * freq for val, freq in most)
            ans.append(checksum)

        return ans
