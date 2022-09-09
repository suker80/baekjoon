#include <iostream>
using namespace std;

int n,k,t,q,a,b;
static const int MAX = 123456;
static const int MIN = -123456;
int maxtree[400123] , mintree[400123];
int swap_arr[100001];

int max_init(int node,int left,int right){

    if (left == right){
    maxtree[node] = left;
    return maxtree[node];}
    int mid = (left + right)/2;
    int m1 = max_init(node * 2, left, mid);
    int m2 = max_init(node * 2 + 1, mid + 1, right);
    maxtree[node] = max(m1, m2);
    return maxtree[node];
}
int max_update(int node,int left,int right,int index,int val){
    if(left > index || index > right){
        return maxtree[node];
    }

    if(left == right && left ==index){
        maxtree[node] = val;
        return maxtree[node];
    }
    int mid = (left + right)/2;
    int m1 = max_update(node * 2, left, mid,index,val);
    int m2 = max_update(node * 2 + 1, mid + 1, right,index,val);
    maxtree[node] = max(m1, m2);
    return maxtree[node];
}
int max_query(int node ,int left ,int right, int start ,int end){
    if (left > end || start >right){
        return MIN;
    }
    if(left >= start && right <= end){
        return maxtree[node];
    }
    int mid = (left+right)/2;
    int m1 = max_query(node*2,left,mid,start,end);
    int m2 = max_query(node*2+1,mid+1,right,start,end);
    return max(m1,m2);
}
int min_init(int node,int left,int right){

    if (left == right){
    mintree[node] = left;
    return mintree[node];}
    int mid = (left + right)/2;
    int m1 = min_init(node * 2, left, mid);
    int m2 = min_init(node * 2 + 1, mid + 1, right);
    mintree[node] = min(m1, m2);
    return mintree[node];
}
int min_update(int node,int left,int right,int index,int val){
    if(left > index || index > right){
        return mintree[node];
    }

    if(left == right && left ==index){
        mintree[node] = val;
        return mintree[node];
    }
    int mid = (left + right)/2;
    int m1 = min_update(node * 2, left, mid,index,val);
    int m2 = min_update(node * 2 + 1, mid + 1, right,index,val);
    mintree[node] = min(m1, m2);
    return mintree[node];
}
int min_query(int node ,int left ,int right, int start ,int end){
    if (left > end || start >right){
        return MAX;
    }
    if(left >= start && right <= end){
        return mintree[node];
    }
    int mid= (left+right)/2;
    int m1 = min_query(node*2,left,mid,start,end);
    int m2 = min_query(node*2+1,mid+1,right,start,end);
    return min(m1,m2);
}
int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>t;
    for(int i =0; i<t; i++){
        cin>>n>>k;
        max_init(1,1,n);
        min_init(1,1,n);
        for(int i = 0; i<n+1;i++) swap_arr[i] = i;
        for(int j =0; j<k; j++){
            int q,a,b;
            cin >> q>>a>>b;
            a +=1;
            b+=1;

            if(q==0){
                max_update(1, 1, n, a, swap_arr[b]);
                max_update(1, 1, n, b, swap_arr[a]);
                min_update(1, 1, n, a, swap_arr[b]);
                min_update(1, 1, n, b, swap_arr[a]);
                int temp = swap_arr[a];
                swap_arr[a] = swap_arr[b];
                swap_arr[b] = temp;
            }
            else{
                int max_res = max_query(1,1,n,a,b);
                int min_res = min_query(1,1,n,a,b);
                if(max_res == b && min_res == a){
                    cout<<"YES"<<'\n';
                }
                else{
                   cout << "NO" << '\n';
                }
            }
        }
    }
  
}