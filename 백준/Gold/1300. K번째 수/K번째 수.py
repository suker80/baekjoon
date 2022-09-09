n = int(input())
k = int(input())

s,e = 1,k

while s<= e:
    mid = (s+e)//2
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n,mid//i)
    if cnt < k:
        s = mid+ 1
    else:
        e = mid-1
print(s)
        
        