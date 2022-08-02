import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int dy, dx;
            int count = 0;
            int y, x;

            int[][] arr = new int[n][n];
            int dir = 0;
            Stack<int[]> stack = new Stack<>();
            stack.push(new int[]{0, 0, dir});
            while (count < n * n) {
                int[] pop = stack.pop();
                y = pop[0];
                x = pop[1];
                dir = pop[2];
                dy = direction[dir][0];
                dx = direction[dir][1];

                arr[y][x] = ++count;
                int ny = dy + y;
                int nx = dx + x;
                if (ny < n && nx < n && 0 <= ny && 0 <= nx && arr[ny][nx] == 0) {
                    stack.push(new int[]{ny, nx, dir});
                } else {
                    dir = (dir + 1) % 4;
                    dy = direction[dir][0];
                    dx = direction[dir][1];
                    ny = dy + y;
                    nx = dx + x;
                    stack.push(new int[]{ny, nx, dir});
                }


            }

            System.out.printf("#%d\n", i + 1);
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    System.out.printf("%d ", arr[j][k]);
                }
                System.out.println();

            }
        }


    }
}

