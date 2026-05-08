class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(list)

        for i, num in enumerate(nums):
            d = 2
            tmp = num
            while d * d <= tmp:
                if tmp % d == 0:
                    mp[d].append(i)
                    while tmp % d == 0:
                        tmp //= d
                d += 1
            if tmp > 1:
                mp[tmp].append(i)

        visited = [False] * n
        q = deque()
        q.append(0)
        count = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                num = nums[i]
                if visited[i]:
                    continue
                visited[i] = True
                if i == n - 1:
                    return count
                if num in mp:
                    for x in mp[num]:
                        q.append(x)
                    del mp[num]
                if i + 1 < n:
                    q.append(i + 1)
                if i - 1 >= 0:
                    q.append(i - 1)

            count += 1

        return count
