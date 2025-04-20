class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        count = 0

        for rabbit, val in counter.items():
            rabbit += 1
            group = ceil(val / rabbit)
            count += rabbit * group

        return count
