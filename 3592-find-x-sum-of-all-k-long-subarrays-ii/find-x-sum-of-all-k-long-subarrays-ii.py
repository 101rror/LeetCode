class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = Counter()
        top = SortedList()
        rest = SortedList()
        tsum = 0
        ans = []

        def balance():
            nonlocal tsum
            while len(top) < x and rest:
                f, v = rest.pop()
                top.add((f, v))
                tsum += f * v
            while len(top) > x:
                f, v = top.pop(0)
                tsum -= f * v
                rest.add((f, v))
            while rest and top and rest[-1] > top[0]:
                f1, v1 = rest.pop()
                f2, v2 = top.pop(0)
                tsum += f1 * v1 - f2 * v2
                top.add((f1, v1))
                rest.add((f2, v2))

        def add(num):
            nonlocal tsum
            old = (freq[num], num)
            if old in top:
                top.remove(old)
                tsum -= old[0] * old[1]
            elif old in rest:
                rest.remove(old)
            freq[num] += 1
            new = (freq[num], num)
            rest.add(new)
            balance()

        def remove(num):
            nonlocal tsum
            old = (freq[num], num)
            if old in top:
                top.remove(old)
                tsum -= old[0] * old[1]
            else:
                rest.remove(old)
            freq[num] -= 1
            if freq[num] > 0:
                rest.add((freq[num], num))
            else:
                del freq[num]
            balance()

        for i in range(k):
            add(nums[i])
        ans.append(tsum)

        for i in range(k, len(nums)):
            remove(nums[i - k])
            add(nums[i])
            ans.append(tsum)

        return ans
