import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, m;
    static int start, end;

    public static void main(String[] args) throws IOException {
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        StringBuilder sb = new StringBuilder();

        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] prefix = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + array[i - 1];
        }
        for (int i = 0; i < m; i++) {
            String[] query = br.readLine().split(" ");
            start = Integer.parseInt(query[0]);
            end = Integer.parseInt(query[1]);
            sb.append(prefix[end] - prefix[start - 1]);
            sb.append("\n");
        }
        System.out.println(sb);


    }
}
