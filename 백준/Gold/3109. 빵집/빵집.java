import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int r, c;
    private static char[][] board;
    private static int[][] direction = {{-1, 1}, {0, 1}, {1, 1}}, visit;
    private static int answer;

    public static void main(String[] args) throws IOException {
        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        r = array[0];
        c = array[1];
        board = new char[r][];
        visit = new int[r][c];

        for (int i = 0; i < r; i++) {
            board[i] = br.readLine().toCharArray();
        }
        for (int i = 0; i < r; i++) {
            solve(i, 0);
        }
        System.out.println(answer);

    }

    private static boolean solve(int y, int x) {
        visit[y][x] = 1;
        if (x == c - 1) {
            answer += 1;
            return true;
        }

        for (int[] dir : direction) {
            int ny = y + dir[0];
            int nx = x + dir[1];

            if (0 <= ny && ny < r && 0 <= nx && nx < c && visit[ny][nx] == 0 && board[ny][nx] == '.') {
                boolean flag = solve(ny, nx);
                if (flag) {
                    return true;
                }
            }
        }
        return false;}


}
