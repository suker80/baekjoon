#include<bits/stdc++.h>
 
using namespace std;
 
#define Max 14
 
int n, m, c, dp[1 << Max][11][21];
vector<int> v;
 
/*
n : 보석의 개수
m : 가방의 개수
c : 가방의 최대 한도
*/
 
int dfs(int path, int idx, int cap)
{
    // 모든 보석 또는 모든 가방을 사용했다면 return 0;
    if ((path == (1 << n) - 1) || idx == m) {
        return 0;
    }
 
    int &ret = dp[path][idx][cap];
    if (ret != -1) {
        return ret;
    }
 
    ret = 0;
 
    for (int i = 0; i < n; i++) {
        if ((path & (1 << i)) || cap < v[i]) {
            continue;
        }
 
        if (cap - v[i] > 0) {
            ret = max(ret, dfs(path | (1 << i), idx, cap - v[i]) + 1);
        }
 
        ret = max(ret, dfs(path | (1 << i), idx + 1, c) + 1);
    }
 
    return ret;
}
 
int main()
{
    cin.tie(0);
 
    memset(dp, -1, sizeof(dp));
 
    scanf("%d %d %d", &n, &m, &c);
 
    v.assign(n, 0);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
 
    printf("%d\n", dfs(0, 0, c));
 
    return 0;
}