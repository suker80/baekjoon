import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {

            int n = Integer.parseInt(br.readLine());
            int[][] farm = new int[n][n];
            for (int j = 0; j < n; j++) {
                String line = br.readLine();
                for (int k = 0; k < n; k++) {
                    farm[j][k] = line.charAt(k) - '0';
                }
            }
            int answer = 0;
            int mid = n / 2;
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (Math.abs(j - mid) + Math.abs(k - mid) <= mid) {
                        answer += farm[j][k];
                    }

                }

            }


            System.out.printf("#%d %d\n", i + 1, answer);
        }
    }
}
