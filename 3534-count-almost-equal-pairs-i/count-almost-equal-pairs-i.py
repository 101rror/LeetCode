class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n - 1):
            for j in range(i + 1, n):

                n1 = str(nums[i])
                n2 = str(nums[j])

                if len(n1) < len(n2):
                    n1 = '0' * (len(n2) - len(n1)) + n1

                if len(n1) > len(n2):
                    n2 = '0' * (len(n1) - len(n2)) + n2

                count = 0

                for k in range(len(n2)):
                    if n1[k] != n2[k]:
                        count += 1

                if count <= 2 and sorted(n1) == sorted(n2):
                    ans += 1

        return ans
