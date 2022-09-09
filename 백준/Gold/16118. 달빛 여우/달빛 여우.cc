#include <bits/stdc++.h>
using namespace std;

typedef pair<int, double> p1; //graph
typedef pair<double, int> p2; //pq

vector<double> dijkstra(vector<p1> *g, int n, int s){
	vector<double> dist(n+10, 1e9+7);
	dist[s] = 0;
	priority_queue<p2> pq;
	pq.push({0, s});
	while(!pq.empty()){
		int now = pq.top().second;
		double cost = -pq.top().first;
		pq.pop();
		if(cost > dist[now]) continue;
		for(auto i : g[now]){
			int nxt = i.first;
			double nxtCost = i.second + cost;
			if(dist[nxt] > nxtCost){
				dist[nxt] = nxtCost;
				pq.push({-nxtCost, nxt});
			}
		}
	}
	return dist;
}

void make_graph(vector<p1> *prv, vector<p1> *nxt, int n){
	for(int i=1; i<=n; i++){
		for(int j=0; j<prv[i].size(); j++){
			auto now = prv[i][j];
			nxt[2*i].push_back({now.first*2+1, now.second/2});
			nxt[2*i+1].push_back({now.first*2, now.second*2});
		}
	}
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	int n, m; cin >> n >> m;
	vector<p1> g[10000], g1[10000];

	for(int i=0; i<m; i++){
		int a, b, c; cin >> a >> b >> c;
		g[a].push_back({b, c});
		g[b].push_back({a, c});
	}

	make_graph(g, g1, n); //fast:2n		slow:2n+1

	auto d1 = dijkstra(g, n, 1);
	auto tmp = dijkstra(g1, n*2, 2);
	vector<double> d2(n+1);
	for(int i=1; i<=n; i++){
		if(tmp[i*2] == 0 || tmp[i*2] == 1e9+7) d2[i] = tmp[i*2+1];
		else if(tmp[i*2+1] == 0 || tmp[i*2+1] == 1e9+7) d2[i] = tmp[i*2];
		else d2[i] = min(tmp[i*2], tmp[i*2+1]);
	}

	int cnt = 0;
	for(int i=2; i<=n; i++){
		if(d1[i] < d2[i]) cnt++;
	}
	cout << cnt;
}