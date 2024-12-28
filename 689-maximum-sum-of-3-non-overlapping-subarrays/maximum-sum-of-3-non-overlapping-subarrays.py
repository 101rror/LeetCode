class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = [sum(nums[:k])]

        for i in range(1, n - k + 1):
            x = sum(nums[i : i + k])
            window.append(x)

        wlen = len(window)

        left = [0] * wlen
        right = [0] * wlen

        bestleft = 0
        for i in range(wlen):
            if window[i] > window[bestleft]:
                bestleft = i
            left[i] = bestleft

        bestright = wlen - 1
        for i in range(wlen - 1, -1, -1):
            if window[i] >= window[bestright]:
                bestright = i
            right[i] = bestright

        maxsum = 0
        ans = [-1, -1, -1]

        for i in range(k, wlen - k):
            l, r = left[i - k], right[i + k]

            threesum = window[l] + window[i] + window[r]
            if threesum > maxsum:
                maxsum = threesum
                ans = [l, i, r]

        return ans
