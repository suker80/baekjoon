import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n, m, answer;
    private static int[] comb = new int[3];

    private static int[] combVisit;
    private static int[][] visit;
    private static int[][] origBoard, board;
    private static int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};


    public static void main(String[] args) throws IOException {

        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = array[0];
        m = array[1];
        combVisit = new int[n * m];
        origBoard = new int[n][];
        board = new int[n][];
        for (int i = 0; i < n; i++) {
            origBoard[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        combination(0, 0);
        System.out.println(answer);

    }


    private static void combination(int start, int count) {
        if (count == 3) {
            for (int i = 0; i < n; i++) {
                board[i] = origBoard[i].clone();
            }
            for (int k = 0; k < comb.length; k++) {
                int y = comb[k] / m;
                int x = comb[k] % m;
                board[y][x] = 1;

            }

            visit = new int[n][m];
            int temp = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (visit[i][j] == 0 && board[i][j] == 2) {
                        bfs(i, j);
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (board[i][j] == 0) {
                        temp += 1;

                    }
                }
            }
            answer = Math.max(answer, temp);
            return;
        }
        for (int i = start; i < n * m; i++) {
            int y = i / m;
            int x = i % m;
            if (combVisit[i] == 0 && origBoard[y][x] == 0) {
                comb[count] = i;
                combination(i + 1, count + 1);
                comb[count] = 0;
            }

        }

    }

    private static void bfs(int i, int j) {
        Deque<int[]> deque = new ArrayDeque<>();
        deque.addLast(new int[]{i, j});
        while (!deque.isEmpty()) {
            int[] ints = deque.removeFirst();
            int y = ints[0];
            int x = ints[1];

            for (int[] dir : direction) {
                int ny = y + dir[0];
                int nx = x + dir[1];
                if (0 <= ny && ny < n && 0 <= nx && nx < m && visit[ny][nx] == 0 && board[ny][nx] == 0) {
                    visit[ny][nx] = 1;
                    board[ny][nx] = 2;
                    deque.addLast(new int[]{ny, nx});
                }
            }
        }
    }
}
