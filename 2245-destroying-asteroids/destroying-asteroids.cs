public class Solution {
    public bool AsteroidsDestroyed(int mass, int[] asteroids) {
        Array.Sort(asteroids);

        long m = mass;
        foreach (int x in asteroids) {
            if (m < x) {
                return false;
            }
            m += x;
        }

        return true;
    }
}