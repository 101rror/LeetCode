class Solution:
    def fractionAddition(self, expression: str) -> str:
        mp = list(map(int, re.findall(r'[+-]?\d+', expression)))
        num = 0
        den = 1
        
        for i in range(0, len(mp), 2):
            n, d = mp[i], mp[i + 1]
            num = num * d + n * den
            den *= d
        
        common = gcd(num, den)

        return f"{num // common}/{den // common}"