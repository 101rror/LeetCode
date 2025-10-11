class Solution {
    public long maximumTotalDamage(int[] power){
        TreeMap<Integer, Long> dp = new TreeMap<>();
        for(int P : power){
            dp.put(P, dp.getOrDefault(P, 0L) + P);
            dp.put(P - 3, Math.max(0L, dp.getOrDefault(P - 3, 0L)));
        }
        
        long maxAns = 0 , last = 0;
        
        for(int P : dp.keySet()){
            dp.put(P, last = Math.max(dp.get(P) + dp.getOrDefault(P - 3, 0L), last));
            maxAns = Math.max(maxAns , last);
        }
        
        return maxAns;
    }
}