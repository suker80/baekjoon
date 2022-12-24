import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;

import static java.lang.Math.max;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n, d, k;
    private static Integer coupon;

    public static void main(String[] args) throws IOException {
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        n = input[0];
        d = input[1];
        k = input[2];
        coupon = input[3];
        int[] array = new int[n];
        int count = 0;
        int[] counter = new int[d + 1];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            int i1 = Integer.parseInt(br.readLine());
            array[i] = i1;
        }
        for (int i = 0; i < n + k; i++) {
            if (i < k) {
                if (counter[array[i]] == 0) {
                    count += 1;
                }
                counter[array[i]] += 1;
                answer = max(answer, count);
            } else {
                int first = array[i - k];
                counter[first] -= 1;
                if (counter[first] == 0) {
                    count -= 1;
                }
                if (counter[array[i % n]] == 0) {
                    count += 1;
                }
                counter[array[i % n]] += 1;
                if (counter[coupon] > 0) {
                    answer = max(answer, count);
                } else {
                    answer = max(answer, count + 1);
                }
            }
        }
        System.out.println(answer);


    }
}
