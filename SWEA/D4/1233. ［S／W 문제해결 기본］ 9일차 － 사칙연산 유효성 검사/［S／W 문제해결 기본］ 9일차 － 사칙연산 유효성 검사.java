import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        for (int t = 0; t < 10; t++) {
            int n = Integer.parseInt(br.readLine());
            int answer = 1;
            String op = "+-*/";
            for (int i = 0; i < n; i++) {
                String[] s = br.readLine().split(" ");
                if (s.length > 2) {
                    if (!op.contains(s[1])) {
                        answer = 0;
                    }
                } else {
                    for (int j = 2; j < s.length; j++) {
                        if (op.contains(s[j])) {
                            answer = 0;
                        }
                    }
                }

            }
            System.out.printf("#%d %d\n", t + 1, answer);

        }

    }


}
