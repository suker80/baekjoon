

#include <cstdio>

#include <algorithm>

#include <vector>

#include <queue>

using namespace std;

#define INF (long long)1e18

int N, M;

long long S, E;

struct Home {

    int v;

    long long len;

    bool stock;

    Home() {}

    Home(int vv, long long ll, bool ss) :v(vv), len(ll), stock(ss) {}

};

vector<Home> adj[5001];

long long dijkstra(int start) {

    vector<long long> dist(N + 1, INF);

    priority_queue<pair<long long, int>> pq;

 

    dist[start] = 0;

    pq.push({ 0,start });

    while (!pq.empty()) {

        int here = pq.top().second;

        long long cost = -pq.top().first;

        pq.pop();

 

        if (dist[here] < cost) continue;

        for (auto const &n : adj[here]) {

            int next = n.v;

            long long len = n.len;

            if (n.stock) {

                long long ncost;

                if (dist[here] < S) {

                    if (dist[here] + len >= S) {

                        long long diff = S - dist[here];        //S시간보다 작을 때 일반속도로 감

                        long long last = len - diff;

                        long long st = min(E - S, last * 2);        //S시간이상 E시간 미만일때 정체속도

                        long long fin = last - st / 2;                    //E시간보다 커졌을 때 일반속도

                        ncost = dist[here] + diff + st + fin;

                    }

                    else {

                        ncost = dist[here] + len;

                    }

                }

                else {

                    if (dist[here] >= E) {

                        ncost = dist[here] + len;

                    }

                    else {

                        long long st = min(E - dist[here], len * 2);

                        long long last = len - st / 2;

                        ncost = dist[here] + st + last;

                    }

                }

                if (dist[next] > ncost) {

                    dist[next] = ncost;

                    pq.push({ -ncost,next });

                }

            }

            else {

                long long ncost = dist[here] + len;

                if (dist[next] > ncost) {

                    dist[next] = ncost;

                    pq.push({ -ncost,next });

                }

            }

        }

    }

    long long ret = 0;

    for (int n = 1;n <= N;n++) {

        ret = max(ret, dist[n]);

    }

    return ret;

}

int main() {

    scanf("%d%d%lld%lld", &N, &M, &S, &E);

    S *= 2, E *= 2;

    for (int m = 0;m < M;m++) {

        int u, v, l, t1, t2;

        scanf("%d%d%d%d%d", &u, &v, &l, &t1, &t2);

        adj[u].emplace_back(Home(v, (long long)l*2, t1));

        adj[v].emplace_back(Home(u, (long long)l*2, t2));

    }

    long long ans = dijkstra(1);

    if (ans & 1) printf("%lld.5\n", ans / 2);

    else printf("%lld\n", ans / 2);

    return 0;

}    
