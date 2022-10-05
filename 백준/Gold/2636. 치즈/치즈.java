import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n, m;

    private static int[][] board;
    private static ArrayDeque<int[]> deque = new ArrayDeque<>();
    private static int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static void main(String[] args) throws IOException {
        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = array[0];
        m = array[1];
        board = new int[n + 2][m + 2];
        for (int i = 1; i < n; i++) {
            int[] array1 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j = 0; j < array1.length; j++) {
                int i1 = array1[j];
                board[i][j + 1] = i1;
            }
        }
        int time = 0;
        int prev = 0;
        int count = check();
        while (count > 0) {
            solve();
            prev = count;
            count = check();
            time += 1;
        }
        System.out.println(time);
        System.out.println(prev);

    }

    private static void solve() {

        deque.add(new int[]{0, 0});
        int[][] visit = new int[n + 2][m + 2];
        visit[0][0] = 1;
        ArrayList<int[]> cheese = new ArrayList<>();
        while (!deque.isEmpty()) {
            int[] ints = deque.removeFirst();
            int y = ints[0];
            int x = ints[1];
            for (int[] dir : direction) {
                int ny = y + dir[0];
                int nx = x + dir[1];
                if (0 <= ny && ny < n+2 && 0 <= nx && nx < m+2 && visit[ny][nx] == 0) {
                    if (board[ny][nx] == 0) {
                        deque.add(new int[]{ny, nx});
                    } else {
                        cheese.add(new int[]{ny, nx});
                    }
                    visit[ny][nx] = 1;
                }
            }
        }
        for (int[] ints : cheese) {
            int y = ints[0];
            int x = ints[1];
            board[y][x] = 0;
        }
    }

    private static int check() {
        int count = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 1) {
                    count++;
                }
            }
        }
        return count;
    }
}
