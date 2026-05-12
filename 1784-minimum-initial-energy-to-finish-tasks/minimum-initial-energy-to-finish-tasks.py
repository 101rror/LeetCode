class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda task: task[1] - task[0], reverse=True)

        cur, ans = 0, 0

        for actual, minimum in tasks:
            if cur < minimum:
                ans += minimum - cur
                cur = minimum
            cur -= actual

        return ans
