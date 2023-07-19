class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        ans = 0
        i = 0

        while (i < n):
            letter = chars[i]
            count = 0
            
            while (i < n and chars[i] == letter):
                count += 1
                i += 1

            chars[ans] = letter
            ans += 1

            if (count > 1):
                for j in str(count):
                    chars[ans] = j
                    ans += 1

        return ans