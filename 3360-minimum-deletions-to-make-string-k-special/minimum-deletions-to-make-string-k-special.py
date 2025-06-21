class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def delete(num, res = 0):
            for x in counter:
                if x < num:
                    res += x
                if x > num + k:
                    res += x - num - k

            return res

        counter = Counter(word).values()

        return min(map(delete, counter))
