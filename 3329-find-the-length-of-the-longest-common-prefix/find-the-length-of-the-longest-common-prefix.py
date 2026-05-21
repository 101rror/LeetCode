class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0

        for num in arr1:
            x = str(num)
            temp = ""

            for char in x:
                temp += char
                mp[temp] += 1

        for num in arr2:
            x = str(num)
            temp = ""

            for char in x:
                temp += char
                if temp in mp:
                    ans = max(ans, len(temp))

        return ans
