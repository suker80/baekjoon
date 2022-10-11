import sun.nio.ch.SelectorImpl;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Solution {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n, k, answer;
    private static int[][] board;

    public static void main(String[] args) throws IOException {
        int testcase = Integer.parseInt(br.readLine());
        for (int t = 0; t < testcase; t++) {
            int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            n = array[0];
            k = array[1];
            board = new int[n][];
            answer = 0;
            for (int i = 0; i < n; i++) {
                board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            }
            for (int i = 0; i < n; i++) {
                check(board[i]);
                int finalI = i;
                check(IntStream.range(0, n).map(j -> board[j][finalI]).toArray());
            }
            System.out.printf("#%d %d\n", t + 1, answer);


        }


    }

    private static void check(int[] arr) {
        int flag = 1;
        int count = 1;
        int curHeight = arr[0];
        for (int i = 1; i < n; i++) {
            if (Math.abs(curHeight - arr[i]) > 1) {
                flag = 0;
            } else if (arr[i] - curHeight == 1) {
                if (count >= k) {
                    curHeight = arr[i];
                    count = 1;
                } else {
                    flag = 0;
                }
            } else if (curHeight - arr[i] == 1) {
                for (int j = 0; j < k; j++) {
                    if (!(i + j < n && arr[i] == arr[i + j])) {
                        flag = 0;
                        break;
                    }
                }

                curHeight = arr[i];
                count = -k + 1;
            } else if (arr[i] == curHeight) {
                count += 1;
            }
        }
        if (flag > 0) {
            answer += flag;
        }
    }
}
