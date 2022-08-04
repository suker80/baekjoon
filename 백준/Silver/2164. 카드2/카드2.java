import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static Deque<Integer> deque = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            deque.add(i + 1);
        }

        while (deque.size() > 1) {
            deque.pollFirst();
            Integer integer = deque.pollFirst();
            deque.addLast(integer);

        }

        System.out.println(deque.pop());

    }
}
