import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final Map<String, Boolean> visit = new HashMap<>();
    private static int n;
    private static int[] p;
    private static int[] s, cur;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        p = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        s = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        cur = new int[n];
        for (int i = 0; i < n; i++) {
            cur[i] = i % 3;
        }
        int count = 0;
        while (true) {
            if (check()) {
                System.out.println(count);
                break;
            }
            swap();
            visit();
            count += 1;
        }

    }

    public static boolean check() {
        for (int i = 0; i < p.length; i++) {
            if (cur[i] != p[i]) {

                return false;
            }
        }
        return true;
    }

    public static void swap() {
        int[] newArr = new int[n];
        for (int i = 0; i < s.length; i++) {
            newArr[i] = cur[s[i]];
        }
        cur = newArr;
    }

    public static void visit() {
        StringBuilder sb = new StringBuilder();
        for (int i : cur) {
            sb.append(i);
        }
        String key = sb.toString();
        if (visit.containsKey(key)) {
            System.out.println(-1);
            System.exit(0);
        } else {
            visit.put(key, true);
        }
    }

}