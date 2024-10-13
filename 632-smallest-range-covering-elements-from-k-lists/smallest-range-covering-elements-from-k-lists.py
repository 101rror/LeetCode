class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ordered = []

        for k, lst in enumerate(nums):
            for n in lst:
                ordered.append((n, k))

        ordered.sort()

        n = len(ordered)
        ans = []
        map = defaultdict(int)
        count, j = 0, 0

        for i in range(n):
            if map[ordered[i][1]] == 0:
                count += 1
            map[ordered[i][1]] += 1

            if count == len(nums):
                while map[ordered[j][1]] > 1:
                    map[ordered[j][1]] -= 1
                    j += 1

                if not ans or ans[1] - ans[0] > ordered[i][0] - ordered[j][0]:
                    ans = [ordered[j][0], ordered[i][0]]

        return ans