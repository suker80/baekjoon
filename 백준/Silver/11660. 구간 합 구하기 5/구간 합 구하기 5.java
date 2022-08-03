import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, m;
    static int x1, x2, y1, y2, answer;

    public static void main(String[] args) throws IOException {
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        StringBuilder sb = new StringBuilder();
        int[][] prefix = new int[n + 1][n + 1];
        for (int i = 0; i < n; i++) {
            int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            for (int j = 0; j < n; j++) {
                prefix[i + 1][j + 1] = array[j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j];
            }
        }

        for (int i = 0; i < m; i++) {
            int[] query = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            y1 = query[0];
            x1 = query[1];
            y2 = query[2];
            x2 = query[3];
            answer = prefix[y2][x2] - prefix[y2][x1 - 1] - prefix[y1 - 1][x2] + prefix[y1 - 1][x1 - 1];
            sb.append(answer).append("\n");
        }
        System.out.println(sb);


    }
}
