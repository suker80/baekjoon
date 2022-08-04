import java.io.*;
import java.util.Stack;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {

        for (int i = 0; i < 10; i++) {
            int n = Integer.parseInt(br.readLine());
            Stack<Character> stack = new Stack<>();
            char[] chars = br.readLine().toCharArray();

            System.out.printf("#%d ", i + 1);
            solve(stack, chars);


        }

    }


    static void solve(Stack<Character> stack, char[] chars) {
        for (char aChar : chars) {
            if (aChar == '(' | aChar == '{' | aChar == '[' | aChar == '<') {
                stack.push(aChar);
            } else if (aChar == ')') {
                Character pop = stack.pop();
                if (pop != '(') {
                    System.out.println(0);
                    return;
                }
            } else if (aChar == '}') {
                Character pop = stack.pop();
                if (pop != '{') {
                    System.out.println(0);
                    return;
                }
            } else if (aChar == '>') {
                Character pop = stack.pop();
                if (pop != '<') {
                    System.out.println(0);
                    return;
                }
            } else if (aChar == ']') {
                Character pop = stack.pop();
                if (pop != '[') {
                    System.out.println(0);
                    return;
                }
            }
        }


        if (stack.isEmpty()) {
            System.out.println(1);

        }
    }
}
