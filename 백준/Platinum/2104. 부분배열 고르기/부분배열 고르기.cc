#include <iostream>
using namespace std;
#define ll long long
 
const int nMax = 100000;
int n, arr[nMax];
ll DnC(int s, int e)
{
    int l, r, height;
    ll base;
    if (s == e)
        return (ll)arr[s] * arr[s];
    int mid = (s + e) / 2;
    ll m = max(DnC(s, mid), DnC(mid + 1, e));
 
    // from here on, the length of the array is at least more than 1 (>=2)
    // find base here so that you don't have to make the same addition again.
    l = mid;
    r = mid + 1;
    base = arr[l] + arr[r];
    height = min(arr[l], arr[r]);
    m = max(m, base * height);
 
    while (!(l == s && r == e))
    {
        // look closely at how to set the conditions and order! think hard!
        // the basic of the computer programming:
        // by saving a value in a variable, you can track down the history
        if (r < e && (l == s || arr[l - 1] < arr[r + 1]))
        {
            base += arr[++r];
            height = min(height, arr[r]);
        }
        else
        {
            base += arr[--l];
            height = min(height, arr[l]);
        }
        m = max(m, base * height);
    }
    return m;
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    cout << DnC(0, n - 1) << '\n';
    return 0;
}