n = int(input())
cnt = 0
values = [int(_) for _ in input().split() ]
for v in values:
    if v==1:
        continue
    for i in range(2,v):
        if v%i == 0:
            break
    else:
        cnt +=1
print(cnt)
    
        
    