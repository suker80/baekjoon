import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n;
    private static int[][] board;

    private static int[][][] rate = new int[4][5][5];
    private static int[][] direction = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};
    private static int move = 1;
    private static int y, x, dir, dy, dx, ny, nx;
    private static int answer;
    private static int sy;
    private static int sx;
    private static int moveCount = 1;

    public static void main(String[] args) throws IOException {

        n = Integer.parseInt(br.readLine());

        rate[0] = new int[][]{{0, 0, 2, 0, 0,}, {0, 10, 7, 1, 0}, {5, 0, 0, 0, 0}, {0, 10, 7, 1, 0}, {0, 0, 2, 0, 0}};

        board = new int[n][n];
        y = n / 2;
        x = n / 2;
        dir = 0;
        for (int i = 1; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    rate[i][j][k] = rate[i - 1][k][5 - 1 - j];
                }
            }

        }
        for (int i = 0; i < n; i++) {
            board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        while (moveCount <= board.length) {
            for (int i = 0; i < moveCount; i++) {

                dy = direction[dir][0];
                dx = direction[dir][1];
                ny = y + dy;
                nx = x + dx;
                if (0 <= ny && ny < n && 0 <= nx && nx < n) {
                    sandMove();
                }
                y = ny;
                x = nx;
            }
            dir = (dir + 1) % 4;
            if (dir % 2 == 0) {
                moveCount += 1;
            }
        }
        System.out.println(answer);
    }

    private static void sandMove() {
        int[][] tempRate = rate[dir];
        int sand = board[ny][nx];
        int remainSand = 0;
        int sandY, sandX;

        for (int i = 0; i < tempRate.length; i++) {
            for (int j = 0; j < tempRate.length; j++) {
                sandY = ny + i - 2;
                sandX = nx + j - 2;
                int calcSand = calcSand(sand, tempRate[i][j]);
                remainSand += calcSand;

                if (0 > sandY || 0 > sandX || sandY >= n || sandX >= n) {
                    answer += calcSand;
                } else {
                    board[sandY][sandX] += calcSand;
                }
            }
        }
        board[ny][nx] = 0;
        if (0 <= ny + dy && ny + dy < n && 0 <= nx + dx && nx + dx < n) {
            board[ny + dy][nx + dx] += sand - remainSand;
        } else {
            answer += (sand - remainSand);
        }

    }

    private static int calcSand(int sand, int rate) {
        if (rate == 0) {
            return 0;
        }
        return (sand * rate / 100);
    }
}