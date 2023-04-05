import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n, size = 2, seconds = 0;
    private static int[][] graph;
    private static int[] shark;
    private static final int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private static int eatFish = 0;
    private static Comparator<int[]> comparator = (ints1, t1) -> {
        if (ints1[0] != t1[0]) {
            return Integer.compare(ints1[0], t1[0]);
        } else {
            return Integer.compare(ints1[1], t1[1]);
        }
    };


    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        graph = new int[n][];
        for (int i = 0; i < n; i++) {
            graph[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 9) {
                    shark = new int[]{i, j, 0};
                    graph[i][j] = 0;
                }
            }
        }
        while (true) {
            int[] solve = solve(shark);
            int ny = solve[0];
            int nx = solve[1];
            int dist = solve[2];

            graph[ny][nx] = 0;
            eatFish += 1;
            seconds += dist;
            shark = new int[]{ny, nx, 0};
            if (eatFish == size) {
                eatFish = 0;
                size += 1;
            }

        }

    }

    private static int[] solve(int[] shark) {
        int[][] visit = new int[n][n];

        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.add(shark);
        ArrayList<int[]> fish = new ArrayList<>();
        int fishDist = Integer.MAX_VALUE;
        int[] ints = new int[0];
        while (!queue.isEmpty()) {
            ints = queue.pollFirst();
            int y = ints[0];
            int x = ints[1];
            visit[y][x] = 1;
            int dist = ints[2];
            if (dist == fishDist) {
                break;
            }
            for (int[] dir : direction) {
                int ny = y + dir[0];
                int nx = x + dir[1];

                if (0 <= ny && ny < n && 0 <= nx && nx < n && visit[ny][nx] == 0) {
                    if (graph[ny][nx] >= 1 && graph[ny][nx] < size) {
                        fishDist = dist + 1;
                        fish.add(new int[]{ny, nx, fishDist});
                    }
                    if (graph[ny][nx] <= size) {
                        queue.add(new int[]{ny, nx, dist + 1});
                    }
                    visit[ny][nx] = 1;
                }
            }
        }
        Collections.sort(fish, comparator);

        if (!fish.isEmpty()) {
            return fish.get(0);
        } else {
            System.out.println(seconds);
            System.exit(0);
        }
        return null;
    }
}
