import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int[][] board;
    private static int r, c, t;
    private static final int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private static final int[][] UpperCleaner = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    private static final int[][] LowerCleaner = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    private static ArrayDeque<Dust> dustQueue = new ArrayDeque<>();

    private static List<int[]> cleaner = new ArrayList<>();


    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        board = new int[r][];
        for (int i = 0; i < r; i++) {
            board[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == -1) {
                    cleaner.add(new int[]{i, j});
                }
            }
        }

        for (int i = 0; i < t; i++) {
            dustMove();
            clean();

        }
        int sum = 0;
        for (int i = 0; i < r; i++) {
            sum += Arrays.stream(board[i]).sum();
        }
        System.out.println(sum + 2);


    }

    private static void clean() {
        cleanUpper();
        cleanLower();

    }

    private static void cleanUpper() {
        int[] upperCleaner = cleaner.get(0);
        int y = upperCleaner[0] - 1;
        int x = upperCleaner[1];
        int dir = 0;

        while (true) {
            int ny = UpperCleaner[dir][0] + y;
            int nx = UpperCleaner[dir][1] + x;

            if (0 <= ny && ny <= upperCleaner[0] && 0 <= nx && nx < c) {
                if (board[ny][nx] == -1) {
                    board[y][x] = 0;
                    break;
                }
                board[y][x] = board[ny][nx];
                y = ny;
                x = nx;
            } else {
                dir += 1;
                ny = UpperCleaner[dir][0] + y;
                nx = UpperCleaner[dir][1] + x;
                board[y][x] = board[ny][nx];

                y = ny;
                x = nx;
            }

        }
    }

    private static void cleanLower() {
        int[] lowerCleaner = cleaner.get(1);
        int y = lowerCleaner[0] + 1;
        int x = lowerCleaner[1];
        int dir = 0;

        while (true) {
            int ny = LowerCleaner[dir][0] + y;
            int nx = LowerCleaner[dir][1] + x;

            if (lowerCleaner[0] <= ny && ny < r && 0 <= nx && nx < c) {
                if (board[ny][nx] == -1) {
                    board[y][x] = 0;
                    break;
                }
                board[y][x] = board[ny][nx];
                y = ny;
                x = nx;
            } else {
                dir += 1;
                ny = LowerCleaner[dir][0] + y;
                nx = LowerCleaner[dir][1] + x;
                board[y][x] = board[ny][nx];

                y = ny;
                x = nx;
            }

        }
    }

    private static void dustMove() {
        int[][] nextBoard = new int[r][];
        for (int i = 0; i < r; i++) {
            nextBoard[i] = board[i].clone();
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] >= 5) {
                    dustQueue.add(new Dust(i, j));
                }
            }
        }
        while (!dustQueue.isEmpty()) {
            Dust ints = dustQueue.removeFirst();
            int y = ints.y;
            int x = ints.x;
            int moveDust = board[y][x];


            for (int[] value : direction) {
                int ny = y + value[0];
                int nx = x + value[1];
                if (0 <= ny && ny < r && 0 <= nx && nx < c && board[ny][nx] != -1) {
                    nextBoard[ny][nx] += moveDust / 5;
                    nextBoard[y][x] -= moveDust / 5;
                }
            }

        }
        board = nextBoard;

    }

    private static class Dust {
        int y;
        int x;

        @Override
        public int hashCode() {
            return y * 1000 + x;
        }

        @Override
        public boolean equals(Object obj) {
            return obj.hashCode() == this.hashCode();
        }

        public Dust(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
