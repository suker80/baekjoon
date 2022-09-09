#include <iostream>
#include <algorithm>

using namespace std;

long long tree[300000];
long long arr[100010];

long long init(int node, int start, int end) {

	if (start == end) return tree[node] = arr[start];
	
	int mid = (start + end) / 2;

	return tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end);
}

void update(int node, int start, int end, long long diff, int index) {

	if (index < start || index > end) return;

	tree[node] += diff;

	int mid = (start + end) / 2;
	if (start != end) {
		update(node * 2, start, mid, diff, index);
		update(node * 2 + 1, mid + 1, end, diff, index);
	}
	return;
}

long long sum(int node, int start, int end, int left, int right) {

	int mid = (start + end) / 2;

	if (left > end || right < start) return 0;
	else if (left <= start && end <= right) return tree[node];
	else return sum(node * 2, start, mid, left, right) + sum(node * 2 + 1, mid + 1, end, left, right);
}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int N, Q; cin >> N >> Q;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	init(1, 0, N - 1);

	for (int i = 0; i < Q; i++) {
		int x, y, a, b;
		cin >> x >> y >> a >> b;
		int n1 = min(x, y);
		int n2 = max(x, y);

		cout << sum(1, 0, N - 1, n1-1, n2-1) << '\n';
		long long diff = b - arr[a - 1];
		arr[a - 1] = b;
		update(1, 0, N - 1, diff, a - 1);
	}

	return 0;
}