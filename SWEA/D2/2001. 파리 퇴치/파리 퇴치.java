

import java.io.*;
import java.util.Arrays;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n, m;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        int testcase = Integer.parseInt(br.readLine());
        for (int t = 1; t <= testcase; t++) {
            int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            n = array[0];
            m = array[1];
            board = new int[n][];
            for (int j = 0; j < n; j++) {
                board[j] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
            int answer = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j <n; j++) {
                    answer = Math.max(answer, cal(i, j));
                }
            }

            System.out.printf("#%d %d\n", t, answer);

        }
    }

    static int cal(int i, int j) {
        int temp = 0;
        for (int k = 0; k < m; k++) {
            for (int l = 0; l < m; l++) {
                if (i + k >= n | j + l >= n) {
                    return 0;
                } else {
                    temp += board[i + k][j + l];
                }
            }
        }
        return temp;

    }
}
