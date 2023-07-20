import java.lang.*;
import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        int answer = 0;
        int[] dp = new int[1000001];
        Arrays.fill(dp,Integer.MAX_VALUE);
        dp[x] = 0;
        for(int i = x; i<1000001; i++){
            int min = Integer.MAX_VALUE;
            if(i - n >=0){
                min = Math.min(min,dp[i-n]);
            }
            if(i % 2 ==0){
                min = Math.min(min,dp[i/2]);
            }
            if(i % 3 ==0){
                min = Math.min(min,dp[i/3]);
            }
            if(min < Integer.MAX_VALUE){
                dp[i] = min + 1;
            }

        }
        if (dp[y] == Integer.MAX_VALUE) {
            return -1;
        }
        return dp[y];
    }
}