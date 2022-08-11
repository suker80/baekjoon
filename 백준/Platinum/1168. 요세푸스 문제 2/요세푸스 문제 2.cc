#include <iostream>
using namespace std;

int find_idx;
int tree[400012];

int init(int node ,int left ,int right){
    if (left==right)
    {
        tree[node] = 1;
        return tree[node];
    }

    int mid = (left+right) /2;
    tree[node] = init(node*2,left,mid) + init(node*2+1,mid+1,right);
    return tree[node];
    
}

int update(int node ,int left ,int right,int i){
    if (i>right | i<left)
    {
        return tree[node];
    }
    if (left==right && left ==i)
    {
        tree[node] =0;
        return tree[node];
    }
    
    int mid = (left+right) /2;
    int m1 =update(node*2,left,mid,i);
    int m2= update(node*2+1,mid+1,right,i);
    tree[node] =m1 + m2;
    return tree[node];
    
}

int query(int node ,int left, int right, int remain){
    if(tree[node] == 0) return 0;
    if (left==right)
    {
        find_idx = left;
        return 1;
    }

    if (remain<=0)
    {
        return 0;
    }
    
    if (tree[node] < remain)
    {
        find_idx = right;
        return tree[node];
    }

    int mid =(left+right)/2;
    int m1 = query(node*2,left,mid,remain);
    m1 = max(0,m1);
    if (remain - m1> 0)
    {
        int m2 = query(node*2+1,mid+1,right,remain-m1);
        return m1+m2;
    }
    else return m1;
    
    
    
}
int main(int argc, char const *argv[])
{
    int n, k;
    cin >>n>>k;
    init(1,1,n);
    int next_index = 1;
    cout<<"<";
    for(int i =n; i>0; i--){
        next_index += k-1;
        if(next_index % i ==0){
            next_index = i;
        }
        else{
            next_index %= i;
        }
        query(1,1,n,next_index);
        if(i == 1){
            cout<<find_idx;
        }
        else{
            cout<<find_idx<<", ";
        }
        update(1,1,n,find_idx);
    }
    cout<<">";
    return 0;
}

