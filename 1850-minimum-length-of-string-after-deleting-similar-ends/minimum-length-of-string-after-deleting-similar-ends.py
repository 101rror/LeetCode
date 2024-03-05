class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        first, last = 0, n - 1
        
        if n == 1:
            return 1

        while first < last and s[first] == s[last]:
            check = s[first]

            while first <= last and s[first] == check:
                first += 1

            while first <= last and s[last] == check:
                last -= 1

        return last - first + 1  