import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n;
    private static int[][] board;
    private static int[] visit;
    private static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        board = new int[n][];
        visit = new int[n];
        for (int i = 0; i < n; i++) {
            board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        for (int i = 0; i < n; i++) {
            visit[i] = 1;
            tsp(0, i, i, 0);
            visit[i] = 0;
        }
        System.out.println(answer);

    }

    private static void tsp(int count, int node, int start, int dist) {
        if (count == n-1) {
            int end_dist = board[node][start];
            if (end_dist != 0) {
                answer = Math.min(dist + end_dist, answer);
            }
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visit[i] == 0 && board[node][i] != 0) {
                visit[i] = 1;
                tsp(count + 1, i, start, dist + board[node][i]);
                visit[i] = 0;
            }
        }

    }
}
