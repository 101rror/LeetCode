class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        first, last = 0, (n - 1)

        while first <= last:
            mid = (first + last) // 2

            if letters[mid] <= target:
                first = mid + 1

            else:
                last = mid - 1

        return letters[first % n]
