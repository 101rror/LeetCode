class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = collections.defaultdict(int)
        left, count, ans = 0, 0, 0
        ln = len(fruits)

        for i in range(0, ln):
            map[fruits[i]] += 1
            count += 1

            while(len(map) > 2):
                f = fruits[left]
                map[f] -= 1
                count -= 1
                left += 1

                if not map[f]:
                    map.pop(f)

            ans = max(ans, count)

        return ans
