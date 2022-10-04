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
    private static HashSet<Integer>[] VerticalSet, HorizontalSet, areaSet;

    public static void main(String[] args) throws IOException {
        VerticalSet = new HashSet[9];
        HorizontalSet = new HashSet[9];
        areaSet = new HashSet[9];
        for (int i = 0; i < 9; i++) {
            VerticalSet[i] = new HashSet<>();
            HorizontalSet[i] = new HashSet<>();
            areaSet[i] = new HashSet<>();
        }
        for (int i = 0; i < 9; i++) {
            String line = br.readLine();
            for (int j = 0; j < 9; j++) {
                board[i][j] = line.charAt(j) - '0';
                VerticalSet[i].add(board[i][j]);
                HorizontalSet[j].add(board[i][j]);
                areaSet[(i / 3) * 3 + j / 3].add(board[i][j]);
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
                int areaIdx = (i / 3) * 3 + j / 3;
                for (int n = 1; n <= 9; n++) {
                    if (!HorizontalSet[j].contains(n) && !VerticalSet[i].contains(n) && !areaSet[areaIdx].contains(n)) {

                        board[i][j] = n;
                        HorizontalSet[j].add(n);
                        VerticalSet[i].add(n);
                        areaSet[areaIdx].add(n);
                        solve(i * 9 + j, depth + 1);
                        HorizontalSet[j].remove(n);
                        VerticalSet[i].remove(n);
                        areaSet[areaIdx].remove(n);
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
