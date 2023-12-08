class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n):
            for j in range(1, n):
                if (i != j and ((arr[i] == arr[j] + arr[j]) or (arr[i] + arr[i] == arr[j]))):
                    return True
                    break
        else:
            return False