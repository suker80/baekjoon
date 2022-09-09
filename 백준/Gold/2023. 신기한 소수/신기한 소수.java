import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        solve(n);
    }

    private static void solve(int i) {
        ArrayList<Integer> answer = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        stack.add(2);
        stack.add(3);
        stack.add(5);
        stack.add(7);
        while (!stack.empty()) {
            int num = stack.pop();
            if (Math.pow(10, n - 1) <= num && num < Math.pow(10, n)) {
                answer.add(num);
            }
            for (int j = 0; j < 10; j++) {
                int newNum = num * 10 + j;
                boolean check = true;
                for (int k = 2; k < Math.sqrt(newNum) + 1; k++) {
                    if (newNum % k == 0) {
                        check=false;
                        break;
                    }

                }
                if (check) {
                    stack.add(newNum);
                }
            }
        }
        Collections.sort(answer);
        answer.forEach(System.out::println);
    }
}
