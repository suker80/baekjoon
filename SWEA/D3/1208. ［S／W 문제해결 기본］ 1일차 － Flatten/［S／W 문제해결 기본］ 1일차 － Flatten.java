import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        public static void main(String[] args) throws IOException {
            for (int k = 0; k < 10; k++) {
                int parseInt = Integer.parseInt(br.readLine());

                StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
                int[] arr = new int[100];

                for (int i = 0; i < 100; i++) {
                    arr[i] = Integer.parseInt(stringTokenizer.nextToken());
                }


                int[] count = new int[101];

                for (int i : arr) {
                    count[i] += 1;
                }
                System.out.printf("#%d ", k + 1);
                solve(parseInt, count);

            }


        }

        private static void solve(int parseInt, int[] count) {
            for (int i = 0; i < parseInt; i++) {
                extracted(count);
            }

            for (int i = 0; i < 100; i++) {
                if (count[i] > 0) {
                    for (int j = 100; j > 0; j--) {

                        if (count[j] > 0) {

                            System.out.println(j - i);
                            return;
                        }
                    }

                }

            }

        }

        private static void extracted(int[] count) {
            for (int j = 100; j > 0; j--) {
                if (count[j] > 0) {
                    for (int k = 0; k < 101; k++) {

                        if (j == k) {
                            return;
                        }

                        if (count[k] > 0) {
                            count[j] -= 1;
                            count[j - 1] += 1;
                            count[k] -= 1;
                            count[k + 1] += 1;
                            return;
                        }

                    }


                }
            }
        }

}

