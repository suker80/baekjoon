N = int(input())


cnt= 0
for i in range(1,N+1):
    while i % 5 ==0:
        i /=5
        cnt += 1 
print(cnt)