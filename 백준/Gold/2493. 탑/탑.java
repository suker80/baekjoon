import java.io.*;
import java.util.Arrays;
import java.util.Stack;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static Stack<int[]> stack = new Stack<>();
    static int index, height;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] answer = new int[n];

        for (int i = n - 1; i > 0; i--) {
            while (!stack.empty() && stack.peek()[0] < array[i]) {
                int[] peek = stack.peek();
                height = peek[0];
                index = peek[1];

                if (array[i] > height) {
                    stack.pop();
                    answer[index] = i + 1;
                }
            }

            if (array[i] > array[i - 1]) {
                stack.push(new int[]{array[i], i});
            } else {
                answer[i] = i;
            }

        }
        while (!stack.empty()) {
            int[] pop = stack.pop();
            height = pop[0];
            index = pop[1];

            if (array[0] > height) {
                answer[index] = 1;
            }
        }
        for (int i = 0; i < n; i++) {
            sb.append(answer[i]).append(" ");
        }
        System.out.println(sb);

    }
}
