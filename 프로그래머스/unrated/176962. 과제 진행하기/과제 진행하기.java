import java.util.*;
import java.lang.*;

class Solution {
    public static String[] solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        Stack<Object[]> stack = new Stack<>();

        for (int i = 0; i < plans.length; i++) {
            String[] time = plans[i][1].split(":");
            plans[i][1] = String.valueOf(Integer.valueOf(time[0]) * 60 + Integer.valueOf(time[1]));
        }
        Arrays.sort(plans, Comparator.comparing(s -> Integer.parseInt(s[1])));

        String[] top = plans[0];
        int i = 1;
        String name = top[0];
        int curTime = Integer.parseInt(top[1]);
        int playTime = Integer.parseInt(top[2]);
        while (i < plans.length) {

            top = plans[i];
            int nextStartTime = Integer.parseInt(top[1]);
            int nextPlayTime = Integer.parseInt(top[2]);
            String nextName = top[0];

            if (nextStartTime < curTime + playTime) {
                stack.add(new Object[]{name, curTime, playTime - (nextStartTime - curTime)});
                curTime = nextStartTime;
                playTime = nextPlayTime;
                name = nextName;
                i++;
            } else {
                answer.add(name);
                if (stack.isEmpty()) {
                    playTime = nextPlayTime;
                    curTime = nextStartTime;
                    name = nextName;
                    i++;
                } else {
                    curTime += playTime;
                    if (curTime == nextStartTime) {
                        name = nextName;
                        playTime = nextPlayTime;
                        i++;

                    }else {

                        Object[] plan = stack.pop();
                        name = (String) plan[0];
                        playTime = (int) plan[2];
                    }
                }

            }
            if (i == plans.length) {
                answer.add(name);
            }

        }
        while (!stack.isEmpty()) {
            answer.add((String) stack.pop()[0]);
        }


        return answer.toArray(new String[0]);
    }
}