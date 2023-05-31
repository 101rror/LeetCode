class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        
        salary.remove(max(salary))
        salary.remove(min(salary))
        
        return sum(salary)/len(salary)