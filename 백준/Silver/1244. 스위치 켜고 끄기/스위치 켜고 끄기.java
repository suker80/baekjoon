import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] array = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            array[i + 1] = Integer.parseInt(st.nextToken());
        }
        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            if (gender == 1) {
                for (int j = num; j < n + 1; j += num) {
                    array[j] = array[j] ^ 1;
                }
            } else {
                int min = Math.min((num - 1), n - num);
                array[num] = array[num] ^ 1;

                for (int j = 1; j < min + 1; j++) {
                    if (array[num - j] == array[num + j]) {
                        array[num - j] = array[num - j] ^ 1;
                        array[num + j] = array[num + j] ^ 1;
                    } else {
                        break;
                    }


                }

            }
        }
        for (int i = 1; i < n + 1; i++) {
            System.out.print(array[i] + " ");
            if (i % 20 == 0) {
                System.out.println();
            }

        }

    }
}
