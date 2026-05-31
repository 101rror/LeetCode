class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        mx = max(asteroids)

        while asteroids:
            ans = []
            for x in asteroids:
                if mass < x:
                    ans.append(x)
                else:
                    mass += x

            if len(ans) == len(asteroids):
                return False
                
            asteroids = ans

        return True
