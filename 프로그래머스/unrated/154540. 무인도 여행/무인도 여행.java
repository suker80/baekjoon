import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Solution {
    private static int[][] direction = {{1,0},{-1,0},{0,-1},{0,1}};
    private static int[][] visit;
    private static int ny,nx,dy,dx,n,m;
    private static char[][] map;
    public int[] solution(String[] maps) {
        int[] answer = {};
        n = maps.length;
        m = maps[0].length();
        visit = new int[n][m];
        map = new char[n][];
        for(int i =0; i< maps.length; i ++){
            map[i] = maps[i].toCharArray();
        }
        int idx =0;
        List<Integer> answerList = new ArrayList<>();
        for(int i = 0; i<n ; i++){
            for(int j=0; j<m; j++){
                if(map[i][j] !='X' && visit[i][j] ==0){
                    answerList.add(dfs(i, j, Integer.parseInt(String.valueOf(map[i][j]))));
                }
            }
        }
        answerList.sort(Comparator.naturalOrder());
        if (answerList.isEmpty()) {
            answerList.add(-1);
        }
        return answerList.stream().mapToInt(i ->i).toArray();
    }

    public int dfs(int y, int x, int count){
        visit[y][x] = 1;
        for(int[] dir : direction){
            dy = dir[0];
            dx = dir[1];
            ny = y+dy;
            nx = x+dx;

            if(0<= ny && ny < n && 0<=nx && nx<m && map[ny][nx] !='X' && visit[ny][nx] ==0){
                count = dfs(ny, nx, count + Integer.parseInt(String.valueOf(map[ny][nx])));
            }
        }
        return count;
    }
}