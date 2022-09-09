import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] board = new int[101][101];

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int answer= 0;

        for (int i = 0; i < n; i++) {
            int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int y = array[0];
            int x = array[1];
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < 10; k++) {
                    board[y + j][x + k] = 1;
                }
            }



        }
        for (int j = 0; j <= 100; j++) {
            for (int k = 0; k <= 100; k++) {
                if (board[j][k] != 0) {
                    answer += 1;
                }
            }
        }
        System.out.println(answer);


    }
}
