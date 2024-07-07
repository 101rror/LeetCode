class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0

        for i in range(n):
            fi = colors[i]
            se = colors[(i + 1) % n]
            th = colors[(i + 2) % n]
            
            if fi == th and fi != se:
                count += 1

        return count