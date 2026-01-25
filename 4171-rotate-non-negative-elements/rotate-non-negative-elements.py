class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for num in nums:
            if num >= 0:
                ans.append(num)

        if not ans:
            return nums

        n = len(ans)
        k %= n

        rotate = ans[k:] + ans[:k]
        x = 0

        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = rotate[x]
                x += 1

        return nums
