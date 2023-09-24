import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.ListIterator;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            LinkedList<Character> list = new LinkedList<Character>();
            ListIterator<Character> iter = list.listIterator();
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                switch(c) {
                    case '<' :
                        if (iter.hasPrevious()) iter.previous();
                        break;
                    case '>' :
                        if (iter.hasNext()) iter.next();
                        break;
                    case '-' :
                        if (iter.hasPrevious()) {
                            iter.previous();
                            iter.remove();
                        }
                        break;
                    default :
                        iter.add(c);
                }
            }
            StringBuilder sb = new StringBuilder();
            for (Character character : list) {
                sb.append(character);
            }
            System.out.println(sb);
        }
    }
}