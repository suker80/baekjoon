import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int s, p;
    private static String dna;
    private static ArrayDeque<Character> queue = new ArrayDeque<>();


    public static void main(String[] args) throws IOException {

        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        s = array[0];
        p = array[1];
        dna = br.readLine();
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] count = new int[4];
        int answer = 0;
        for (int i = 0; i < s; i++) {
            if (queue.size() < p) {
                queue.add(dna.charAt(i));
                if (dna.charAt(i) == 'A') {
                    count[0] += 1;
                } else if (dna.charAt(i) == 'C') {
                    count[1] += 1;
                } else if (dna.charAt(i) == 'G') {
                    count[2] += 1;
                } else if (dna.charAt(i) == 'T') {
                    count[3] += 1;
                }
            } else {
                char pop = queue.pop();
                if (pop == 'A') {
                    count[0] -= 1;
                } else if (pop == 'C') {
                    count[1] -= 1;
                } else if (pop == 'G') {
                    count[2] -= 1;
                } else if (pop == 'T') {
                    count[3] -= 1;
                }
                queue.add(dna.charAt(i));
                if (dna.charAt(i) == 'A') {
                    count[0] += 1;
                } else if (dna.charAt(i) == 'C') {
                    count[1] += 1;
                } else if (dna.charAt(i) == 'G') {
                    count[2] += 1;
                } else if (dna.charAt(i) == 'T') {
                    count[3] += 1;
                }
            }
            if (queue.size() == p && count[0] >= arr[0] & count[1] >= arr[1] & count[2] >= arr[2] & count[3] >= arr[3]) {
                answer += 1;
            }

        }
        System.out.println(answer);


    }
}
