class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        mp, ans = {}, 0

        for num in arr1:
            x = str(num)
            temp = ''

            for char in x:
                temp += char
                mp[temp] = mp.get(temp, 0) + 1

        
        for num in arr2:
            x = str(num)
            temp = ''

            for char in x:
                temp += char
                if temp in mp:
                    ln = len(temp)
                    ans = max(ans, ln)

        return ans
