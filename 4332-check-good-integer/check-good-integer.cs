public class Solution {
    public bool CheckGoodInteger(int n) {
        int digitSum = 0, squareSum = 0;
        
        while (n > 0) {
            int r = n % 10;
            digitSum += r;
            squareSum += r * r;
            n /= 10;
        }
        
        return (squareSum - digitSum) >= 50;
    }
}