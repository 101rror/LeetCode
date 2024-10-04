class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total = 0

        target = skill[0] + skill[-1]
        itt = 0

        while itt < n // 2:
            check = skill[itt] + skill[-itt - 1]

            if check != target:
                return -1

            total += skill[itt] * skill[-itt - 1]

            itt += 1

        return total
