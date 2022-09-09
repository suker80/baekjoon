#include<iostream>

using namespace std;
int64_t tree[400123], lazy[400123], lazy_size[400123];
int array[100001];
int n, q;

int64_t calc(int a, int s_n, int d) {

    return (s_n * (2 * a + (s_n - 1) * d)) / 2;
}

int64_t init(int node, int left, int right) {
    if (left == right) {
        tree[node] = array[left];
        return tree[node];
    }

    int mid = (left + right) / 2;
    int m1 = init(node * 2, left, mid);
    int m2 = init(node * 2 + 1, mid + 1, right);
    return 0;
}

int64_t update(int node, int left, int right, int start, int end) {
    if (start <= left && right <= end) {
        lazy[node] += left - start + 1;
        lazy_size[node] += 1;
        if (left != right) {
            lazy[node * 2] += lazy[node];
            lazy_size[node * 2] += lazy_size[node];

            lazy[node * 2 + 1] += lazy[node] + ((right - left) / 2 + 1) * lazy_size[node];
            lazy_size[node * 2 + 1] += lazy_size[node];
            lazy_size[node] = 0;
            lazy[node] = 0;
        }
        return tree[node];
    }
    // 첫항이 lazy[node] 이고 공차가 lazy_size[node] 이고 갯수는 right-left+1

    if (lazy[node] != 0) {
        tree[node] += calc(lazy[node], right - left + 1, lazy_size[node]);
        if (left != right) {

            lazy[node * 2] += lazy[node];
            lazy_size[node * 2] += lazy_size[node];

            lazy[node * 2 + 1] += lazy[node] + ((right - left) / 2 + 1) * lazy_size[node];
            lazy_size[node * 2 + 1] += lazy_size[node];

        }
        lazy_size[node] = 0;
        lazy[node] = 0;
    }
    if (left > end or start > right) {

        return tree[node];
    }
    int mid = (left + right) / 2;
    int64_t m1 = update(node * 2, left, mid, start, end);
    int64_t m2 = update(node * 2 + 1, mid + 1, right, start, end);
    return 0;

}

int64_t query(int node, int left, int right, int index) {
    if (index > right or index < left) {
        return 0;
    }

    if (lazy[node] != 0) {
        if (left != right) {

            lazy[node * 2] += lazy[node];
            lazy_size[node * 2] += lazy_size[node];

            lazy[node * 2 + 1] += lazy[node] + ((right - left) / 2 + 1) * lazy_size[node];
            lazy_size[node * 2 + 1] += lazy_size[node];
            lazy_size[node] = 0;
            lazy[node] = 0;
        }

    }
    if (left == right and left == index) {
        tree[node] += lazy[node];
        lazy[node] = 0;
        return tree[node];
    }
    int mid = (left + right) / 2;
    int64_t m1 = query(node * 2, left, mid, index);
    int64_t m2 = query(node * 2 + 1, mid + 1, right, index);
    return m1 + m2;

}

int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> array[i];
        /* code */
    }
    init(1, 1, n);
    cin >> q;
    for (int i = 0; i < q; i++) {
        int c, a, b, index;
        cin >> c;
        if (c == 1) {
            cin >> a >> b;
            update(1, 1, n, a, b);
        } else {
            cin >> index;
            cout << query(1, 1, n, index) << '\n';
        }


    }

    return 0;
}

