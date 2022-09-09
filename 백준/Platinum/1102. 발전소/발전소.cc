#include<algorithm> 
#include<iostream> 
#include<string> 
using namespace std; 
const int INF = 987654321; 
int N, p, cnt, cost[17][17], dp[1 << 17], light, ret; 
string s; 
int go(int light){
    int &ret = dp[light]; 
    if(ret != -1) return ret; 
    if(cnt >= p) return ret = 0; 
    ret = INF; cnt++; 
    for(int i = 0; i < N; i++){
        if(light & (1 << i)){
            for(int j = 0; j < N; j++){
                if(!(light & (1 << j)))ret = min(ret, go(light | (1 << j)) + cost[i][j]);
            }
        }
    }
    cnt--; return ret; 
}
int main(){
    fill(dp, dp + (1 << 17), -1);
    cin >> N; 
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cin >> cost[i][j]; 
        }
    }
    cin >> s >> p;  
    for(int i = 0; i < s.size(); i++){
        if(s[i] == 'Y'){ cnt ++; light |= 1 << i;}
    }
    int ret = go(light); 
    cout << (ret == INF ? -1 : ret) << "\n";   
    return 0;
}