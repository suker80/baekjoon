import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.toSet;

public class Main {
    private static int[][] board = new int[9][9];
    private static int zeroCnt = 0;
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        for (int i = 0; i < 9; i++) {
            String line = br.readLine();
            for (int j = 0; j < 9; j++) {
                board[i][j] = line.charAt(j) - '0';
                if (board[i][j] == 0) {
                    zeroCnt += 1;
                }

            }
        }
        solve(0, 0);


    }

    private static void solve(int index, int depth) {
        if (depth == zeroCnt) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(board[i][j]);
                }
                sb.append('\n');
            }
            System.out.println(sb);
            System.exit(0);
        }

        for (int idx = index; idx < 81; idx++) {
            int i = idx / 9;
            int j = idx % 9;


            if (board[i][j] == 0) {
                int finalJ = j;
                Set<Integer> HorizontalSet = Arrays.stream(board[i]).boxed().collect(toSet());
                Set<Integer> VerticalSet = Arrays.stream(board).map(ints -> ints[finalJ]).collect(toSet());
                Set<Integer> areaSet = new HashSet<>();
                for (int k = (i / 3) * 3; k < (i / 3 + 1) * 3; k++) {
                    for (int l = (j / 3) * 3; l < (j / 3 + 1) * 3; l++) {
                        areaSet.add(board[k][l]);
                    }
                }
                for (int n = 1; n <= 9; n++) {
                    if (!HorizontalSet.contains(n) && !VerticalSet.contains(n) && !areaSet.contains(n)) {
                        board[i][j] = n;
                        solve(i * 9 + j, depth + 1);
                        board[i][j] = 0;
                    }
                }
                return;
            }
        }

    }

    private static boolean check() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }

}
