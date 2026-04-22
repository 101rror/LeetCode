class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def distance(s1, s2):
            n = len(s1)
            cnt = 0

            for i in range(n):
                if s1[i] != s2[i]:
                    cnt += 1
                if cnt == 3:
                    return False

            return True

        good = []

        for query in queries:
            for d in dictionary:
                dist = distance(query, d)
                if dist:
                    good.append(query)
                    break
                    
        return good
