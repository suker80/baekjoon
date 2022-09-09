import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.LocalDate;
import java.time.LocalDateTime;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        int answer= 0;
        for (int i = 2019; i <= n; i++) {
            for (int j = 1; j <= 12; j++) {
                int value = LocalDate.of(i, j, 13).getDayOfWeek().getValue();
                if (value == 5) {
                    answer += 1;
                }
            }
        }
        System.out.println(answer);

    }
}
