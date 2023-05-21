class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        pointer = len(digits) - 1
        
        while digits[pointer] == 9:
            digits[pointer] = 0
            pointer -= 1
        
        if pointer == -1:
            digits.insert(0, 1)
        
        else:
            digits[pointer] += 1
        
        return digits