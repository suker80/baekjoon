import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] direction = {{1, 0}, {0, 1}, {0, -1}};


    public static void main(String[] args) throws IOException {
        for (int k = 0; k < 10; k++) {
            int[][] ladder = new int[100][100];
            int end = 0;
            br.readLine();
            for (int i = 0; i < 100; i++) {
                StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    ladder[i][j] = Integer.parseInt(stringTokenizer.nextToken());
                    if (ladder[i][j] == 2) {
                        end = j;
                    }
                }
            }
            System.out.printf("#%d ", k + 1);
            for (int i = 0; i < 100; i++) {
                if (ladder[0][i] == 1) {
                    boolean isLeft = true;
                    boolean isDown = true;
                    solve(0, i, ladder);

                }
            }
        }

    }

    private static void solve(int y, int start, int[][] ladder) {

        int direction_idx = 0;
        int dy;
        int x;
        int dx;
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{y, start, direction_idx});
        while (!stack.isEmpty()) {
            int[] pop = stack.pop();
            y = pop[0];
            x = pop[1];
            if (y == 99) {
                if (ladder[y][x] == 2) {
                    System.out.println(start);
                }
                break;
            }
            direction_idx = pop[2];


            if (direction_idx == 0) {
                if (x - 1 >= 0 && ladder[y][x - 1] == 1) {
                    stack.push(new int[]{y, x - 1, 2});
                    continue;
                } else if (x + 1 < 100 && ladder[y][x + 1] == 1) {
                    stack.push(new int[]{y, x + 1, 1});
                } else {
                    stack.push(new int[]{y + 1, x, 0});
                }
            } else if (direction_idx == 1) {
                if (ladder[y + 1][x] != 0) {
                    stack.push(new int[]{y + 1, x, 0});
                } else {
                    stack.push(new int[]{y, x + 1, 1});
                }
            } else if (direction_idx == 2) {
                if (ladder[y + 1][x] != 0) {
                    stack.push(new int[]{y + 1, x, 0});
                } else {
                    stack.push(new int[]{y, x - 1, 2});
                }

            }

        }
    }
}
