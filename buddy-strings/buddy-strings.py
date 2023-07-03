class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n1 = len(s)
        n2 = len(goal)

        if(n1 == 2):
            return s[::-1]==goal
        l = []
        if(n1 != n2):
            return False
        if(len(set(s)) < n1 and s == goal):
            return True

        for i in range(n1):
            if (s[i] != goal[i]):
                l.append(s[i] + goal[i])
            if (len(l) > 2):
                return False

        return len(l) == 2 and l[0] == l[1][::-1]