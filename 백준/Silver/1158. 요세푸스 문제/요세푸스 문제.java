import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.stream.IntStream;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, m;
    static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        queue = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        IntStream.range(1, n+1).forEach(queue::add);
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < m - 1; j++) {
                queue.add(queue.poll());
            }
            sb.append(queue.poll()).append(", ");
        }
        sb.append(queue.poll()).append(">");
        System.out.println(sb);

    }
}
