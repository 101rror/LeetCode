class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant = [i for i in range(n) if senate[i] == 'R']
        dire = [j for j in range(n) if senate[j] == 'D']
        
        while (radiant and dire):
            r = radiant.pop(0)
            d = dire.pop(0)

            if (r < d):
                radiant.append(n + r)
            else:
                dire.append(n + d)
                
        return 'Radiant' if radiant else 'Dire'