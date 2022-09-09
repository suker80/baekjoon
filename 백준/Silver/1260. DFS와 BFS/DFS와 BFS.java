import java.io.*;
import java.util.*;

public class Main {

    public static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static List<Integer>[] graph;
    public static int[] visit;
    public static int n, m, v;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = array[0];
        m = array[1];
        v = array[2];

        graph = new ArrayList[n + 1];

        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int a = array[0];
            int b = array[1];
            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 1; i < n + 1; i++) {
            Collections.sort(graph[i]);
        }

        visit = new int[n + 1];
        dfs(v);
        sb.append("\n");
        visit = new int[n + 1];
        bfs(v);
        System.out.println(sb);
    }

    public static void dfs(int x) {
        visit[x] = 1;
        sb.append(x).append(" ");

        for (int y : graph[x]) {
            if (visit[y] == 1) {
                continue;
            }
            dfs(y);
        }
    }

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();

        q.add(start);
        visit[start] = 1;

        while (!q.isEmpty()) {
            int x = q.poll();
            sb.append(x).append(" ");
            for (int y : graph[x]) {
                if (visit[y] == 1) {
                    continue;
                }
                q.add(y);
                visit[y] = 1;
            }
        }
    }
}
