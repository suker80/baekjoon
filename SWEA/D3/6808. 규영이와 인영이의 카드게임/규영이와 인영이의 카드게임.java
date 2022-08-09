import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] GCard, ICard, allCard, visit;
    static int lose, win;

    public static void main(String[] args) throws IOException {
        int testcase = Integer.parseInt(br.readLine());
        for (int t = 0; t < testcase; t++) {
            allCard = new int[19];
            ICard = new int[9];
            visit = new int[9];
            lose = win = 0;
            GCard = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int i = 0; i < GCard.length; i++) {
                allCard[GCard[i]] = 1;
            }
            int idx = 0;
            for (int i = 1; i < 19; i++) {
                if (!(allCard[i] == 1)) {
                    ICard[idx++] = i;
                }
            }
            solve(0, 0, 0);
            System.out.printf("#%d %d %d\n", t + 1, win, lose);
        }


    }

    static void solve(int count, int sum1, int sum2) {
        if (count == 9) {
            if (sum1 > sum2) {
                win += 1;
            } else if (sum1 < sum2){
                lose += 1;
            }
            return;
        }

        for (int i = 0; i < 9; i++) {
            if (visit[i] == 0) {
                visit[i] = 1;

                if (GCard[count] > ICard[i]) {
                    solve(count + 1, sum1 + GCard[count] + ICard[i], sum2);

                } else {
                    solve(count + 1, sum1, sum2 + ICard[i] + GCard[count]);
                }
                visit[i] = 0;
            }
        }
    }
}
