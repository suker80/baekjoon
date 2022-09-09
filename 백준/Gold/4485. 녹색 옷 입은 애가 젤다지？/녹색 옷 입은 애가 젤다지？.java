import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int[][] board, dist;
    private static PriorityQueue<int[]> pq;
    private static int y, x, curDist, ny, nx;
    private static final int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};


    public static void main(String[] args) throws IOException {
        int count = 1;
        while (true) {

            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                break;
            }
            board = new int[n][n];
            dist = new int[n][n];

            for (int i = 0; i < n; i++) {
                board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                Arrays.fill(dist[i], Integer.MAX_VALUE);
            }
            pq = new PriorityQueue<>(Comparator.comparingInt(ints -> ints[2]));
            pq.add(new int[]{0, 0, board[0][0]});

            while (!pq.isEmpty()) {
                int[] poll = pq.poll();
                y = poll[0];
                x = poll[1];
                curDist = poll[2];
                if (curDist > dist[y][x]) {
                    continue;
                }

                for (int[] dir : direction) {
                    ny = y + dir[0];
                    nx = x + dir[1];

                    if (0 <= ny && ny < n && 0 <= nx && nx < n) {
                        if (board[ny][nx] + curDist < dist[ny][nx]) {
                            dist[ny][nx] = board[ny][nx] + curDist;
                            pq.add(new int[]{ny, nx, dist[ny][nx]});
                        }
                    }
                }
            }

            System.out.printf("Problem %d: %d\n", count, dist[n - 1][n - 1]);
            count += 1;
        }

    }
}
