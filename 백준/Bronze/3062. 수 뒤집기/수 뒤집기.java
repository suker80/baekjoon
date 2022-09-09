
import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i= 0; i<n; i++){

            String x1 = sc.next();
            StringBuffer sb = new StringBuffer(x1);
            String x2 = sb.reverse().toString();

            int ans = Integer.parseInt(x1) + Integer.parseInt(x2);

            String ans_str = Integer.toString(ans);
            StringBuffer sb2 = new StringBuffer(ans_str);

            if (sb2.reverse().toString().compareTo(ans_str) == 0)
            {
                System.out.println("YES");
            }
            else
                System.out.println("NO");


        }
    }
}