class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tsum = sum(apple)

        if tsum == sum(capacity):
            return len(capacity)

        capacity.sort(reverse=True)
        count = 0

        while tsum > 0:
            tsum -= capacity[count]
            count += 1

        return count
