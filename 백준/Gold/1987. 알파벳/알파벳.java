import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

import static java.lang.Math.max;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int r, c, ny, nx;
    private static char[][] board;
    private static int[] visit = new int[26];
    private static int answer;
    private static final int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};


    public static void main(String[] args) throws IOException {
        int[] s = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        r = s[0];
        c = s[1];
        board = new char[r][];

        for (int i = 0; i < r; i++) {
            board[i] = br.readLine().toCharArray();
        }
        visit[board[0][0] - 'A'] = 1;
        solve(0, 0, 1);
        System.out.println(answer);

    }

    private static void solve(int y, int x, int count) {
        if (answer < count) {
            answer = count;
        }
        for (int dir = 0; dir < 4; dir++) {
            ny = y + direction[dir][0];
            nx = x + direction[dir][1];

            if (0 <= ny && ny < r && 0 <= nx && nx < c) {
                int next = board[ny][nx] - 'A';
                if (visit[next] == 0) {
                    visit[next] = 1;
                    solve(ny, nx, count + 1);
                    visit[next] = 0;
                }
            }
        }
    }
}
